import { request } from './api.js';

async function loadCelebrationWall() {
  const container = document.getElementById('celebration-container');

  const response = await request('/projects/completed/');
  const data = await response.json();

  const projects = Array.isArray(data) ? data : data.results;

  if (!projects || projects.length === 0) {
    container.innerHTML = '<p style="color: var(--text-muted);">No completed projects yet. Keep building! 💪</p>';
    return;
  }

  container.innerHTML = projects.map(project => `
    <div class="card" style="border-color: var(--green);">
      <h3>🎉 ${project.title}</h3>
      <p class="meta">by ${project.owner} · Completed ${new Date(project.updated_at).toLocaleDateString()}</p>
      <p style="margin-bottom:0.8rem;">${project.description}</p>
      ${project.tech_stack ? `<p style="color: var(--text-muted); font-size:0.85rem;">🛠 ${project.tech_stack}</p>` : ''}
      ${project.github_url ? `<a href="${project.github_url}" target="_blank">View on GitHub →</a>` : ''}
    </div>
  `).join('');
}

loadCelebrationWall();
