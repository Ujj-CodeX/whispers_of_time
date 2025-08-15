<template>
  <div class="min-vh-100 d-flex flex-column align-items-center py-5 gap-2">

    
    <h2 class="text-black mb-4 ps-3 border-start border-4 border-warning text-start fw-bold">
      Cultural Taste from Heritage
    </h2>

   
    <div v-if="dish" class="card w-100 w-md-75 w-lg-50 mb-3 p-4 shadow" style="background-color: #dcdcdc; max-width: 1100px;">
      <h3 class="card-title text-start fw-bold text" style="color: blue; font-family: cursive;">{{ dish.title }}</h3>
      <h6 class="card-title text-start fw-bold text" style="color: green; font-family: cursive;">{{ dish.name }}</h6>

      
      <p class="text-center fw-bold " style="font-size: large; white-space: pre-line;" >{{ dish.description }}</p>

     
      
    </div>

    

    
    <div v-if="dish" class="card w-100 w-md-75 w-lg-50 mb-3 p-3 shadow" style="background-color: #dcdcdc; max-width: 1100px; ">
        <h4 style="font-family: sans-serif; font-weight: bold;">Fact for this Taste</h4>
      <p class="text-center mb-0 fw-bold" style="font-size: 20px; color: green; font-family: cursive;">{{ dish.fun_fact }}</p>
    </div>

    
    <div v-if="dish" class="card w-100 w-md-75 w-lg-50 mb-3 p-3 shadow" style="background-color: #dcdcdc; max-width: 1100px;">
         <h4 style="font-family: sans-serif; font-weight: bold; color: blue;">Recipe for You</h4>
      <iframe
        class="w-100"
        height="315"
        :src="embedYouTube(dish.video_link)"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </div>

   
    <button class="btn btn-success mt-3" @click="markComplete">
       Back To Your Journey
    </button>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CulturalKnowledgePage",
  data() {
    return {
      dish: null,
      isMuted: false
    };
  },
  computed: {
    
  },
  methods: {
    async fetchDish() {
      try {
        const dish_Id = this.$route.params.id; 
        let res = await axios.get(`http://127.0.0.1:5000/api/dish/${dish_Id}`);
        if (res.data) {
          this.dish = res.data;
        }
      } catch (err) {
        console.error("Error fetching dish:", err);
      }
    },
    toggleAudio() {
      const audio = this.$refs.folkAudio;
      if (audio) {
        this.isMuted = !this.isMuted;
        audio.muted = this.isMuted;
      }
    },
    embedYouTube(videoId) {
  if (!videoId) return "";
  return `https://www.youtube.com/embed/${videoId}`;
},
    markComplete() {
      this.$router.push("/");
    }
  },
  mounted() {
    this.fetchDish();
  }
};
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
