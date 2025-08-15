<template>
  <h3 style="font-weight: bold; color: green;">Complete the dishes to unlock surprises and cultural heritage facts!</h3>
  <div class="journey-wrapper">
    
    <div v-if="!regionSelected" class="overlay">
      <div class=" inset-card p-4 text-center">
        <h1 style="font-weight: bold; color: blue;">Welcome to Taste of Heritage</h1>
      <h2 style="font-weight: bold; color: orangered;">Unlock the Secrets of Every Bite!</h2>
      <h4 style="font-weight: bold; color: green;">Choose Region you want to taste</h4>
      <div>
        <img :src="require('@/assets/3.png')" style="height: 100px;  ">
      <select v-model="selectedRegion" style="margin-top: 20px; width: 150px; margin-left: 280px;" class="form-control">
        <option value="" disabled>Select Region</option>
        <option v-for="region in regions" :key="region.id" :value="region.id">
          {{ region.name }}
        </option>
      </select>
      
    </div>
    
      <button class="btn btn-primary" @click="fetchDishes" style="margin-top: 50px; ">Start Journey</button>
    </div>
    </div>

    
    <div v-else class="map-container">
      <svg class="map-svg" width="100%" height="800">
        <template v-for="(item, index) in dishesWithTreasures" :key="index">
          
          <line
            v-if="index < dishesWithTreasures.length - 1"
            :x1="positions[index].x"
            :y1="positions[index].y"
            :x2="positions[index + 1].x"
            :y2="positions[index + 1].y"
            stroke="black"
            stroke-width="5"
            stroke-height
          />
        </template>
      </svg>

      
      <div
  v-for="(item, index) in dishesWithTreasures"
  :key="'point-' + index"
  class="point"
  :class="item.type"
  :style="{ top: positions[index].y + 'px', left: positions[index].x + 'px' }"
  @click="item.type === 'dish' ? goToDish(item.id) : openTreasure(index)"
>
  <template v-if="item.type === 'dish'">
    <div style="text-align: center;">
    <img
      :src="getDishImage(item.image_path)"
      :alt="item.name"
      style="height: 100px; width: 120px; "
    />
    <p style="margin-top: 5px; font-size: 14px; font-weight: bold; color: #333;">
      {{ item.name }}
    </p></div>
  </template>
  <template v-else>
    <img
      src="@/assets/treasure.png"
      alt="Treasure"
      style="height: 100px; width: 100px;"
      @click="openTreasure"
    />
    <p style="margin-top: 5px; font-size: 14px; font-weight: bold; color: orangered;">
      surprise
    </p>
  </template>
</div>
    <div v-if="showTreasureModal" class="overlay">
      <div class=" inset-card p-4 text-center">
        <h1 style="font-weight: bold; color: blue;">Yayy !! Surprise for You</h1>
      <h2 style="font-weight: bold; color: orangered;">Here is an intersting facts for You! {{ currentIndex + 1 }}</h2>
      <h4 style="font-weight: bold; color: green;">Do you Know ?</h4>
      <p v-if="loadingFacts">Loading facts...</p>
      <p style="white-space: pre-line; color: black; font-size: large; font-weight: bold;">{{ treasures[currentIndex].treasure}}</p>
      <div>
        
      <button class="btn btn-danger" @click="showTreasureModal = false">Close</button>
      
    </div>
    </div>
    </div>


    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "JourneyMap",
  data() {
    return {
      treasures: [],
      currentIndex: 1,
      showTreasureModal: false,
      treasureFacts: [],
      loadingFacts: false,
      regions: [],
      selectedRegion: "",
      regionSelected: false,
      dishes: [],
      
      positions: [
        { x: 100,  y: 100 },
  { x: 300,  y: 200 },
  { x: 500,  y: 100 },
  { x: 700,  y: 200 },
  { x: 900,  y: 100 },

  
  { x: 1200,  y: 300 },

  
  { x: 900,  y: 500 },
  { x: 600,  y: 400 },
  { x: 400,  y: 500 },
  { x: 100,  y: 300 },

  
  { x: 100,  y: 500 }
      ]
    };
  },
  computed: {
    dishesWithTreasures() {
      let result = [];
      this.dishes.forEach((dish, idx) => {
        result.push({ ...dish, type: "dish" });
        if ((idx + 1) % 3 === 0 && idx !== this.dishes.length) {
          result.push({ type: "treasure" });
        }
      });
      return result;
    }
  },
  methods: {
    async fetchRegions() {
      try {
        let res = await axios.get("http://127.0.0.1:5000/api/states");
        this.regions = res.data;
      } catch (err) {
        console.error("Failed to fetch regions:", err);
      }
    },
    async fetchDishes() {
      if (!this.selectedRegion) return;
      try {
        let res = await axios.get(
          `http://127.0.0.1:5000/api/dishes?region_id=${this.selectedRegion}`
        );
        this.dishes = res.data.slice(0, 10);
        this.regionSelected = true;
      } catch (err) {
        console.error("Failed to fetch dishes:", err);
      }
    },

    getDishImage(fileName) {
    
    try {
      return require(`@/assets/${fileName}`);
    } catch (error) {
      console.error("Image not found:", fileName);
      return require("@/assets/u.3.png"); 
    }
  },
    goToDish(id) {
      alert("Starting your Journey of Taste " + id);
      this.$router.push({ name: "dash", params: { id } });
    },
    
    openTreasure() {
      this.showTreasureModal = true;
      
    },
    async fetchAllTreasures() {
      try {
        const response = await fetch("http://127.0.0.1:5000/api/treasure");
        this.treasures = await response.json();
      } catch (error) {
        console.error("Error fetching treasures:", error);
      }
    },
    showNextTreasure() {
      if (this.treasures.length > 0) {
        this.showTreasureCard = true;
        this.currentIndex = (this.currentIndex + 1) % this.treasures.length;
      }
    },
  
  },
  mounted() {
    this.fetchAllTreasures();
    this.fetchRegions();
  }
};
</script>

<style scoped>
.journey-wrapper {
  width: 100%;
  min-height: 100vh;
  
}





.overlay {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 800px;
  height: 500px;
  backdrop-filter: blur(8px); 
  background-color: rgba(255, 255, 255, 0.3);
 
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
  z-index: 1000;
}



.map-container {
  position: relative;
  padding: 20px;
}

.map-svg {
  position: absolute;
  top: 50px;
  left: 50px;
}

.point {
  position: absolute;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  
  line-height: 20px;
  font-size: 12px;
  font-weight: bold;
  cursor: pointer;
  color: white;
  
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  
  
}
.point:hover {
  transform: scale(1.15);
  box-shadow: 0 0 12px rgba(255, 112, 67, 0.7);
  z-index: 5;
}
.point.treasure {
  background: orangered;
  font-size: 24px;
}
</style>
