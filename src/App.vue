<template>
    <div id="app" style="background: transparent;">
    <NavBar v-if="$route.name !== 'Login'" />
    
    <main class="container-fluid">
      <router-view />  
    </main>
    </div>
    
   
  
</template>

<script>
import NavBar from './components/Nav.vue';

export default {
  name: 'App',
  components: { NavBar 
  }
}
</script>


<style>
html,body {
  
  background-image: url('@/assets/bg.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;

}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
