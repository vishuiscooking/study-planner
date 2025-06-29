document.addEventListener("DOMContentLoaded", function() {
    const today = new Date();
    document.getElementById("date").innerText = today.toLocaleDateString();
});

function addTask() {
    const taskInput = document.getElementById("taskInput");
    const taskValue = taskInput.value.trim();
    
    if (taskValue === "") {
        alert("Please enter a task.");
        return;
    }

    const li = document.createElement("li");
    li.innerText = taskValue;

    const deleteBtn = document.createElement("button");
    deleteBtn.innerText = "Delete";
    deleteBtn.className = "delete-btn";
    deleteBtn.onclick = function() {
        li.remove();
    };

    li.appendChild(deleteBtn);
    document.getElementById("taskList").appendChild(li);
    taskInput.value = ""; // Clear input field
}

