<script>
    import { loggedIn, currentUser } from './store.js';
  
    let employeeId = '';
    let password = '';
  
    function login() {
      // Simplified: all users use "password" as password
      if (password === 'password' && employeeId.trim() !== '') {
        loggedIn.set(true);
        currentUser.set(employeeId.trim());
      } else {
        alert('Invalid login');
      }
    }
  </script>
  
  <main>
    <h1>Login</h1>
    <label>
      Employee ID:
      <input bind:value={employeeId} />
    </label>
    <br />
    <label>
      Password:
      <input type="password" bind:value={password} />
    </label>
    <br />
    <button on:click={login}>Login</button>
  </main>
  
  <style>
    main {
      max-width: 400px;
      margin: auto;
      padding: 2em;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin-top: 5em;
    }
  </style>
  