<script>
    import { loggedIn, currentUser } from './store.js';
  
    let $currentUser;
    $: currentUser.subscribe(value => $currentUser = value);
  
    const records = [
      { type: 'PTO', hours: 8, date: '2025-05-01' },
      { type: 'VTO', hours: 4, date: '2025-05-10' },
    ];
  
    function logout() {
      loggedIn.set(false);
      currentUser.set('');
    }
  </script>
  
  <main>
    <h1>Welcome, Employee {$currentUser}</h1>
    <button on:click={logout}>Logout</button>
  
    <h2>Time Off Records</h2>
    <table>
      <thead>
        <tr><th>Date</th><th>Type</th><th>Hours</th></tr>
      </thead>
      <tbody>
        {#each records as record}
          <tr>
            <td>{record.date}</td>
            <td>{record.type}</td>
            <td>{record.hours}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </main>
  
  <style>
    main {
      max-width: 800px;
      margin: auto;
      padding: 2em;
    }
  
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1em;
    }
  
    th, td {
      padding: 0.5em;
      border: 1px solid #ccc;
    }
  </style>
  