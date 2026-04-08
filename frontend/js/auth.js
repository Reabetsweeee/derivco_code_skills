import { request } from './api.js';

// ---- LOGIN ----
const loginBtn = document.getElementById('login-btn');
if (loginBtn) {
  loginBtn.addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMsg = document.getElementById('error-msg');

    const response = await request('/auth/login/', 'POST', { username, password });
    const data = await response.json();

    if (response.ok) {
      localStorage.setItem('access_token', data.access);
      localStorage.setItem('refresh_token', data.refresh);
      localStorage.setItem('username', username);
      window.location.href = 'dashboard.html';
    } else {
      errorMsg.style.display = 'block';
      errorMsg.textContent = 'Invalid username or password.';
    }
  });
}

// ---- REGISTER ----
const registerBtn = document.getElementById('register-btn');
if (registerBtn) {
  registerBtn.addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const bio = document.getElementById('bio').value;
    const github_url = document.getElementById('github_url').value;

    const errorMsg = document.getElementById('error-msg');
    const successMsg = document.getElementById('success-msg');

    const response = await request('/auth/register/', 'POST', {
      username, email, password, bio, github_url
    });

    const data = await response.json();

    if (response.ok) {
      successMsg.style.display = 'block';
      successMsg.textContent = 'Account created! Redirecting to login...';
      setTimeout(() => window.location.href = 'login.html', 1500);
    } else {
      errorMsg.style.display = 'block';
      errorMsg.textContent = JSON.stringify(data);
    }
  });
}

// ---- LOGOUT ----
const logoutBtn = document.getElementById('logout-btn');
if (logoutBtn) {
  logoutBtn.addEventListener('click', () => {
    localStorage.clear();
    window.location.href = 'login.html';
  });
}
