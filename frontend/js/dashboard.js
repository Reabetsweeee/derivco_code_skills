import { request, isLoggedIn } from './api.js';

if (!isLoggedIn()) window.location.href = 'login.html';

const username = localStorage.getItem('username');
const navUsername = document.getElementById('nav-username');
if (navUsername) navUsername.textContent = `👋 ${username}`;

// ---- LOGOUT ----
document.getElementById('logout-btn').addEventListener('click', () => {
  localStorage.clear();
  window.location.href = 'login.html';
});

// ---- LOAD MY PROJECTS ----
async function loadMyProjects() {
  const container = document.getElementById('my-projects');
  const response = await request('/projects/');
  const data = await response.json();

  const myProjects = data.results.filter(p => p.owner === username);

  if (myProjects.length === 0) {
    container.innerHTML = '<p style="color: var(--text-muted);">No projects yet. Create your first one!</p>';
    return;
  }

  container.innerHTML = myProjects.map(project => `
    <div class="card">
      <h3>${project.title}</h3>
      <p class="meta">${new Date(project.created_at).toLocaleDateString()}</p>
      <p style="margin-bottom:0.8rem;">${project.description}</p>
      <span class="status status-${project.status}">${project.status.replace('_', ' ')}</span>
    </div>
  `).join('');
}

// ---- CREATE PROJECT ----
document.getElementById('create-proj-btn').addEventListener('click', async () => {
  const title = document.getElementById('proj-title').value;
  const description = document.getElementById('proj-desc').value;
  const tech_stack = document.getElementById('proj-tech').value;
  const github_url = document.getElementById('proj-github').value;
  const status = document.getElementById('proj-status').value;
  const msg = document.getElementById('proj-msg');

  const response = await request('/projects/', 'POST', {
    title, description, tech_stack, github_url, status
  });

  if (response.ok) {
    msg.className = 'alert alert-success';
    msg.style.display = 'block';
    msg.textContent = 'Project created successfully!';
    loadMyProjects();
  } else {
    const data = await response.json();
    msg.className = 'alert alert-error';
    msg.style.display = 'block';
    msg.textContent = JSON.stringify(data);
  }
});

loadMyProjects();
