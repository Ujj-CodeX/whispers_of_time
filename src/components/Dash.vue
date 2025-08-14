<template>
  <div class=" min-vh-100 d-flex flex-column align-items-center py-5 gap-2">
    
    
    <h2 class="text-white mb-4 ps-3 border-start border-4 border-warning  text-start" style="font-family: sans-serif; font-weight: bold;">
      Todays Cultural Knowledge
    </h2>

    <!-- Main Card -->
    <div class="card w-100 w-md-75 w-lg-50 mb-3 p-4 shadow" style="background-color: #dcdcdc; max-width: 1100px;">
      <h3 class="card-title text-start" style="font-family: sans-serif; font-weight: bold; color: black;">Title Here</h3>
      <div class="images">
        Images
      </div>
      <p class="text-center">Description</p>
    </div>

    <!-- Folk Sound Card -->
    <div class="card w-100 w-md-75 w-lg-50 mb-3 p-3 shadow" style="background-color: #dcdcdc; max-width: 1100px;">
      <p class="text-center mb-0">Any Folk Sound Track Related to it</p>
    </div>

    <!-- Facts Card -->
    <div class="card w-100 w-md-75 w-lg-50 mb-3 p-3 shadow" style="background-color: #dcdcdc; max-width: 1100px;">
      <p class="text-center mb-0">Facts of this Cultural Knowledge</p>
    </div>

    <!-- Map Card -->
    <div class="card w-100 w-md-75 w-lg-50 mb-3 p-3 shadow" style="background-color: #dcdcdc; max-width: 1100px;">
      <p class="text-center mb-0">Map Location to Reach Out</p>
    </div>

    <!-- Teaser Card -->
    <div class="card w-100 w-md-75 w-lg-50 mb-3 p-3 shadow" style="background-color: #dcdcdc; max-width: 1100px;">
      <p class="text-center mb-0">What's New tomorrow ?? -->> Open teaser</p>
    </div>

  </div>
</template>

<script>
export default {
  name: "CulturalKnowledgePage"
};
</script>

<style scoped>



.card {
  border-radius: 1rem;
}
</style>
