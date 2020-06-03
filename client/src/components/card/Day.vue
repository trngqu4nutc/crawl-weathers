<template>
  <div class="col-sm-6 col-md-4 col-lg-3 mb-4">
    <div class="card">
      <div class="card-body">
        <h4 class="card-title text-center">{{ weather.day }}</h4>
        <p class="card-title text-center">{{ weather.date }}</p>
      </div>
      <p v-html="weather.img"></p>
      <div class="card-body">
        <h5 class="card-title text-center">{{ weather.desc }}</h5>
        <h2 class="card-title text-center">{{ weather.celsius }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    weather: Object
  }
};
</script>

<style>
</style>