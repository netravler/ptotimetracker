<script>
  import { onMount } from 'svelte';
  let requests = [];

  onMount(async () => {
    const res = await fetch('http://localhost:8000/requests');
    requests = await res.json();
  });
</script>

<h2>Your PTO Requests</h2>
<ul>
  {#each requests as r}
    <li>{r.date} - {r.type}</li>
  {/each}
</ul>
