<template>
  <div class="journey-wrapper">
    
    <div v-if="!regionSelected" class="overlay">
      <div class=" inset-card p-4 text-center">
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

    <!-- Journey Map -->
    <div v-else class="map-container">
      <svg class="map-svg" width="100%" height="800">
        <template v-for="(item, index) in dishesWithTreasures" :key="index">
          <!-- Path lines -->
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

      <!-- Points (absolute over SVG) -->
      <div
        v-for="(item, index) in dishesWithTreasures"
        :key="'point-' + index"
        class="point"
        :class="item.type"
        :style="{ top: positions[index].y + 'px', left: positions[index].x + 'px' }"
        @click="item.type === 'dish' ? goToDish(item.id) : openTreasure(index)"
      >
        <template v-if="item.type === 'dish'">
          {{ item.name }}
        </template>
        <template v-else>
          <img src="@/assets/treasure.png" alt="Treasure" style="height: 100px; width: 100px;"/>
        </template>
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

  // Move downward to second row
  { x: 900,  y: 300 },

  // Second row (Right → Left)
  { x: 700,  y: 300 },
  { x: 500,  y: 300 },
  { x: 300,  y: 300 },
  { x: 100,  y: 300 },

  // Drop to third row (optional treasure)
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
    goToDish(id) {
      alert("Go to dish with ID: " + id);
      // this.$router.push({ name: "DishDetail", params: { id } });
    },
    openTreasure() {
      alert("Fun fact or surprise!");
    }
  },
  mounted() {
    this.fetchRegions();
  }
};
</script>

<style scoped>
.journey-wrapper {
  width: 100%;
  min-height: 100vh;
  
}




/* Normal card on top */
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
  text-align: center;
  line-height: 70px;
  font-size: 12px;
  font-weight: bold;
  cursor: pointer;
  background: #ff7043;
  color: white;
  border: 3px solid #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  
  
}
.point:hover {
  transform: scale(1.15);
  box-shadow: 0 0 12px rgba(255, 112, 67, 0.7);
  z-index: 5;
}
.point.treasure {
  background: gold;
  font-size: 24px;
}
</style>
