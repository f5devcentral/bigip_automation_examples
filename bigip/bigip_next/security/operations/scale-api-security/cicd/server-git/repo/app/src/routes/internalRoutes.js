const express = require("express");
const os = require("os");
const router = express.Router();

router.get("/node-info", (req, res) => {
    const uptimeMinutes = (os.uptime() / 60).toFixed(2);
    const totalRAM = (os.totalmem() / 1024 / 1024 / 1024).toFixed(2);
    const freeRAM = (os.freemem() / 1024 / 1024 / 1024).toFixed(2);

    const nodeInfo = `
Status: OK
Timestamp: ${new Date()}
Message: Node server is running smoothly.

System Information:
-------------------
OS Type: ${os.type()}
Platform: ${os.platform()}
OS Release: ${os.release()}
Total RAM: ${totalRAM} GB
Free RAM: ${freeRAM} GB
CPU Cores: ${os.cpus().length}
CPU Model: ${os.cpus()[0].model}
System Uptime: ${uptimeMinutes} minutes
`;
    res.setHeader("Content-Type", "text/plain");
    res.send(nodeInfo);
});

module.exports = router;
