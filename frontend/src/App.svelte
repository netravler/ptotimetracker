<script>
    import { loggedIn } from './store.js';
    import Login from './Login.svelte';
    import Home from './Home.svelte';
  
    let $loggedIn;
    $: loggedIn.subscribe(value => $loggedIn = value);
  </script>
  
  {#if $loggedIn}
    <Home />
  {:else}
    <Login />
  {/if}
  