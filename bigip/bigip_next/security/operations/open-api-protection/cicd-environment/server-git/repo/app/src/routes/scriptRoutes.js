const express = require("express");
const router = express.Router();

// Sample script data
const scripts = [
  {
    id: "1",
    name: "Script 1",
    description: "Script - 1",
    code: "<script>alert('Script 1')</script>",
    orderNumber: 1,
  },
  {
    id: "2",
    name: "Script 2",
    description: "Script - 2",
    code: "<script>alert('Script 2')</script>",
    orderNumber: 2,
  },
  {
    id: "3",
    name: "Script 3",
    description: "Script - 3",
    code: "<script>alert('Script 3')</script>",
    orderNumber: 3,
  },
  {
    id: "4",
    name: "Script 4",
    description: "Second - 4",
    code: "<script>alert('Script 4')</script>",
    orderNumber: 4,
  },
  {
    id: "5",
    name: "Script 5",
    description: "Second - 5",
    code: "<script>alert('Script 5')</script>",
    orderNumber: 5,
  },
  {
    id: "6",
    name: "Script 6",
    description: "Second - 6",
    code: "<script>alert('Script 6')</script>",
    orderNumber: 6,
  },
  {
    id: "7",
    name: "Script 7",
    description: "Second - 7",
    code: "<script>alert('Script 7')</script>",
    orderNumber: 7,
  },
  {
    id: "8",
    name: "Script 8",
    description: "Second - 8",
    code: "<script>alert('Script 8')</script>",
    orderNumber: 8,
  },
  {
    id: "9",
    name: "Script 9",
    description: "Second - 9",
    code: "<script>alert('Script 9')</script>",
    orderNumber: 9,
  },
];

/**
 * @swagger
 * /script:
 *   get:
 *     summary: Get all scripts
 *     responses:
 *       200:
 *         description: A list of scripts
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/components/schemas/Script'
 */
router.get("/", (req, res) => {
  res.json({ scripts });
});

/**
 * @swagger
 * /script/status:
 *   get:
 *     summary: Get the status of the service
 *     responses:
 *       200:
 *         description: Service status
 *         content:
 *           text/plain:
 *             schema:
 *               type: string
 *               example: "Status: OK\nSWAGGER Version: v1"
 */
router.get("/status", (req, res) => {
  res.setHeader('content-type', 'text/plain');
  res.send("Status: OK\r\nSwagger Version: v1\r\n");
});

/**
 * @swagger
 * /script/{id}:
 *   get:
 *     summary: Get script by ID
 *     parameters:
 *       - name: id
 *         in: path
 *         required: true
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: The requested script
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/Script'
 *       404:
 *         description: Script not found
 */
router.get("/:id", (req, res) => {
  const script = scripts.find((s) => s.id === req.params.id);
  if (script) {
    res.json(script);
  } else {
    res.status(404).json({ message: "Script not found" });
  }
});

/**
 * @swagger
 * /script:
 *   post:
 *     summary: Create a new script
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Script'
 *     responses:
 *       201:
 *         description: Script created successfully
 */
router.post("/", (req, res) => {
  scripts.push({
    ...req.body,
    id: scripts.length,
  });
  res.status(201).json({ message: "Script created successfully." });
});

/**
 * @swagger
 * /script/{id}:
 *   put:
 *     summary: Update an existing script by ID
 *     parameters:
 *       - name: id
 *         in: path
 *         required: true
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Script updated successfully
 *       404:
 *         description: Script not found
 */
router.put("/:id", (req, res) => {
  const scriptIndex = scripts.findIndex((s) => s.id === req.params.id);
  if (scriptIndex !== -1) {
    scripts[scriptIndex] = req.body;
    res.json({ message: "Script updated successfully." });
  } else {
    res.status(404).json({ message: "Script not found" });
  }
});


module.exports = router;
