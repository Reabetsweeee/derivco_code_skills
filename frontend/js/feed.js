import { request } from './api.js';

async function loadFeed() {
  const container = document.getElementById('feed-container');

  const response = await request('/projects/');
  const data = await response.json();

  if (!data.results || data.results.length === 0) {
    container.innerHTML = '<p style="color: var(--text-muted);">No projects yet. Be the first to build!</p>';
    return;
  }

  container.innerHTML = data.results.map(project => `
    <div class="card">
      <h3>${project.title}</h3>
      <p class="meta">by ${project.owner} · ${new Date(project.created_at).toLocaleDateString()}</p>
      <p style="margin-bottom: 0.8rem;">${project.description}</p>
      <span class="status status-${project.status}">${project.status.replace('_', ' ')}</span>
      ${project.github_url ? `<a href="${project.github_url}" target="_blank" style="margin-left:1rem; font-size:0.85rem;">GitHub →</a>` : ''}
    </div>
  `).join('');
}

loadFeed();
