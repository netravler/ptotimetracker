<script>
  let username = '';
  let password = '';
  let error = '';

  async function login() {
    const res = await fetch('http://localhost:8000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    if (!res.ok) {
      error = 'Login failed';
    } else {
      const data = await res.json();
      localStorage.setItem('user', JSON.stringify(data));
      window.location.href = '/dashboard';
    }
  }
</script>

<h2>Login</h2>
<input bind:value={username} placeholder="Username" />
<input bind:value={password} type="password" placeholder="Password" />
<button on:click={login}>Login</button>
<p>{error}</p>

<style>
  input { display: block; margin-bottom: 8px; }
</style>
