const http = require("http");
const fs = require('fs');
const fsp = require('fs').promises;

const noble = require("noble-mac");
// async()=>{
// let noble;
// if (process.platform === 'darwin') {
//     noble = await import('noble-mac');
// } else {
//     noble = await import('noble');
// }
// }
var robot = require('robotjs')


const DEVICE_UUID = "1c9100e0a1f6d98aaad6a8ced798b4e2";
const host = 'localhost';
const port = 8000;
var time_started_scan;

var key_mappings = {
    0: {
        "key":"",
        "modifier":"",
        "press":true
    },
    1: {
        "key":"",
        "modifier":"",
        "press":true
    },
    2: {
        "key":"",
        "modifier":"",
        "press":true
    },
    3: {
        "key":"",
        "modifier":"",
        "press":true
    }
}

function button_action(button_num, press){
    let data = key_mappings[button_num];
    if(data["press"]){
        if(press){
            robot.keyTap(data["key"], data["modifier"]);
        }
    }else{
        if(press){
            robot.keyToggle(data["key"], "down", data["modifier"]);
        }else{
            robot.keyToggle(data["key"], "up", data["modifier"]);
        }
    }
}

function config_save_keybinds(){
    fs.writeFileSync("config.json", JSON.stringify(key_mappings));
}

function load_keybinds(){
    if(fs.existsSync("config.json")){
        const txt = fs.readFileSync("config.json");
        key_mappings = JSON.parse(txt);
    }else{
        config_save_keybinds();
    }
}

var bluetooth_mode = 0;
const bluetooth_mode_mapping = {
    0:()=>"idle",
    1:()=>"discovering devices..." + (Math.round(Date.now() / 1000)-time_started_scan) + "s",
    2:()=>"connected to device",
    3:()=>"initialization complete",
    4:()=>"device not found. failed to connect."
    
}

noble.on('discover', function (peripheral) {
    bluetooth_mode = 1;
    console.log('peripheral discovered (' + peripheral.uuid +
        ') name (' + peripheral.advertisement.localName +
        ') connectable ' + peripheral.connectable + ',' +
        ' RSSI ' + peripheral.rssi + ':');

    if (peripheral.uuid == DEVICE_UUID) {
        noble.stopScanning();

        connect_to_device(peripheral);
        peripheral.connect();
    }
});

function start_device_discovery(){
    time_started_scan = Math.round(Date.now() / 1000);
        // noble.on('stateChange', function (state) {
    //     if (state === 'poweredOn') {
    //         noble.startScanning();
    //     } else {
    //         noble.stopScanning();
    //     }
    // });
    noble.startScanning();
    setTimeout(()=>{
        noble.stopScanning();
        bluetooth_mode=4;
    }, 15000);    
}

function connect_to_device(peripheral) {
    bluetooth_mode = 2;
    peripheral.on('disconnect', () => {
        console.log('Disconnected from', peripheral.advertisement.localName);
        bluetooth_mode = 0;
    });
    peripheral.on('connect', (error) => {
        if (error) {
            console.error('Connection error:', error);
            return;
        }
        console.log('Connected to', peripheral.advertisement.localName);

        peripheral.discoverAllServicesAndCharacteristics((error, services, characteristics) => {
            if (error) {
                console.error('Discovery error:', error);
                return;
            }

            console.log('Services and characteristics discovered');

            const someCharacteristic = characteristics.find(c => c.uuid === 'ffe1');
            if (someCharacteristic) {
                bluetooth_mode=3;
                someCharacteristic.on('data', (data, isNotification) => {
                    var num = data.readUInt8(0);
                    console.log('Data read-' + num);
                    
                    switch(num){
                        case 1: //1 down
                            button_action(0, true);
                            break;
                        case 2:
                            button_action(0, false);
                            break;
                        case 3: //2 down
                            button_action(1, true);
                            break;
                        case 4:
                            button_action(1, false);
                            break;
                        case 5://3 down
                            button_action(2, true);
                            break;
                        case 6:
                            button_action(2, false);
                            break;
                        case 7://4 down
                            button_action(3, true);
                            break;
                        case 8:
                            button_action(3, false);
                            break;
                    }
                });
                someCharacteristic.subscribe(function (error) {
                    console.log(error);
                });
            }else{
                bluetooth_mode = 0;
            }
        });
    });
}

const requestListener = async function (req, res) {
    const url = req.url;
    const method = req.method;
    
    var body_fetched;

    if(url == "/"){
        fsp.readFile(__dirname + "/static/index.html")
            .then(contents => {
                res.setHeader("Content-Type", "text/html");
                res.writeHead(200);
                res.end(contents);
            });
    }else if(url == "/favicon.ico"){
        fsp.readFile(__dirname + "/static/favicon.ico")
            .then(contents => {
                res.setHeader("Content-Type", "image/vnd.microsoft.icon");
                res.writeHead(200);
                res.end(contents);
            });
    }else if(/^\/static\/\w{1,10}.(?:js|css)$/.test(url)){
        const filename = url.split('/')[2];
        const ext = filename.split('.')[1];
        
        fsp.readFile(__dirname + `/static/${filename}`)
            .then(contents => {
                switch(ext){
                    case "js":
                        res.setHeader("Content-Type", "application/javascript");
                        break;
                    case "css":
                        res.setHeader("Content-Type", "text/css");
                }

                res.writeHead(200);
                res.end(contents);
            })
    }else if(url=="/api/status"){
        res.setHeader("Content-Type", "application/json");
        res.writeHead(200);
        res.end(JSON.stringify({
            "msg":bluetooth_mode_mapping[bluetooth_mode](),
            "code": bluetooth_mode
        }));
    }else if(url=="/api/keybind"){
        if(method=="GET"){
            res.setHeader("Content-Type", "application/json");
            res.writeHead(200);
            res.end(JSON.stringify(key_mappings));
        }else if(method=="PUT"){
            body_fetched = (data)=>{
                data = JSON.parse(data);
                
                key_mappings[data["button"]]["key"] = data["key"];
                key_mappings[data["button"]]["modifier"] = data["modifier"];
                config_save_keybinds();
                res.setHeader("Content-Type", "text/plain");
                res.writeHead(200);
                res.end("success");
            };
        }
    }else if(url=="/api/retry_bt"){
        start_device_discovery();
    }else{
        console.log(`redirect failed for ${url}`);
    }
    let body = [];

    req.on('error', err => {
        console.error(err);
      });

    req.on('data', chunk => {
        body.push(chunk);
      });
    req.on('end', () => {
        body = Buffer.concat(body).toString();
        if(body_fetched){
            body_fetched(body);
        }
    });
};

load_keybinds();
start_device_discovery();

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});