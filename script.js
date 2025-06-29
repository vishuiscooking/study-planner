const API_URL = "http://127.0.0.1:8000/api/notes";
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

// Load tasks from backend
async function loadTasks() {
  try {
    const res = await fetch(API_URL);
    const tasks = await res.json();
    taskList.innerHTML = "";
    tasks.forEach(renderTask);
  } catch (err) {
    console.error("Failed to load tasks:", err);
  }
}

// Render one task
function renderTask(task) {
  const li = document.createElement("li");
  li.textContent = task.title;

  const delBtn = document.createElement("button");
  delBtn.textContent = "❌";
  delBtn.onclick = async () => {
    await fetch(`${API_URL}/${task.id}`, { method: "DELETE" });
    loadTasks();
  };

  li.appendChild(delBtn);
  taskList.appendChild(li);
}

// Add new task
async function addTask() {
  const text = taskInput.value.trim();
  if (!text) return;

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: text, content: "none" })
  });

  taskInput.value = "";
  loadTasks();
}

// Set date
document.getElementById("date").textContent = new Date().toLocaleDateString();

// Initial load
loadTasks();


