document.addEventListener('DOMContentLoaded', () => {
    const status_txt = document.getElementById('status_txt');
    const buttons = document.querySelectorAll(".keyboard button");
    const button_txt = document.querySelectorAll(".keyboard button .keys");
    const retry_bt = document.getElementById("retry_bt");
    const alert = document.getElementById("alert");

    var record_keystroke = false;
    var current_button = -1;
    var temp_key = "";
    var temp_modifier = "";
    var old_text = "";

    var alert_handle = 0;
    function show_alert(text, timeout){
        if(alert_handle!=0){
            clearTimeout(alert_handle);
        }
        alert.innerText = text;
        alert.style.opacity = 1;

        alert_handle = setTimeout(()=>{
            alert.style.opacity = 0;
            alert_handle=0;
        }, timeout);
    }
    function check_status(){
        var failed_count = 0;
        const handler = setInterval(() => {
            fetch("/api/status")
                .then(x => x.json())
                .then(data => {
                    const code = data["code"];
                    status_txt.innerText = data["msg"];

                    if (code == 3 || code==4) {
                        clearInterval(handler);
                        if(code==4){
                            retry_bt.removeAttribute("hidden");
                        }
                    }
                    failed_count = 0;
                })
                .catch(() => {
                    failed_count++;
                    if (failed_count > 2) {
                        clearInterval(handler);
                    }
                });
        }, 500);
    }

    retry_bt.addEventListener("click", ()=>{
        fetch("/api/retry_bt", {method:"POST"});
        retry_bt.setAttribute("hidden", "");
        check_status();
    });

    function keytext(key, modifier) {
        var key_name = {
            "control": "ctrl",
            "command": "cmd"
        }
        if (key_name[modifier]) {
            modifier = key_name[modifier];
        }

        if (modifier.length == 0) {
            return key;
        } else {
            return `${modifier} + ${key}`;
        }
    }

    function send_keydata(){
        const data = {
            "button":current_button,
            "key":temp_key,
            "modifier":temp_modifier
        };
        // publish keybind
        fetch("/api/keybind", {
            method: "PUT", 
            body:JSON.stringify(data)})
            .then(x => {
                if(x.status==200){
                    console.log("successfully updated keybind");
                }else{
                    console.log(`error ${x.status}`);
                }
            });
    }

    for (var i = 0; i < buttons.length; i++) {
        const num = i;
        buttons[num].addEventListener('click', () => {
            if (record_keystroke && current_button == num) { //same button pressed
                record_keystroke = false;
                
                if(temp_key.length==0 && temp_modifier.length==0){
                    button_txt[num].innerText = old_text;
                    show_alert(`canceled keybind`, 2000);
                }else{
                    show_alert(`applied keybind for button ${num}`, 2000);
                    send_keydata();
                }
                current_button = -1;
                buttons[num].classList.remove("selected");

            } else {
                if (current_button != -1) { //new key pressed. reverse operation
                    buttons[current_button].classList.remove("selected");
                    button_txt[current_button].innerText = old_text;
                }
                old_text = button_txt[num].innerText;
                buttons[num].classList.add("selected");
                record_keystroke = true;
                current_button = num;
                temp_key = "";
                temp_modifier = "";
                button_txt[num].innerText = keytext("", "");
            }
        });
    }

    fetch("/api/keybind")
        .then(x => x.json())
        .then(data => {
            for (var i = 0; i < buttons.length; i++) {
                button_txt[i].innerText = keytext(data[i.toString()]["key"], data[i.toString()]["modifier"]);
            }
        });

    document.addEventListener('keydown', function (event) {
        const key = event.key.toLowerCase();
        if (record_keystroke) {
            event.preventDefault();
            if (/^[A-z0-9]$/.test(key)) {
                temp_key = key;
            }

            if (event.shiftKey) {
                temp_modifier = "shift";
            } else if (event.ctrlKey) {
                temp_modifier = "control";
            } else if (event.metaKey) {
                temp_modifier = "command";
            } else if (event.altKey) {
                temp_modifier = "alt";
            }
            button_txt[current_button].innerText = keytext(temp_key, temp_modifier);
        }
    });

    check_status();
});