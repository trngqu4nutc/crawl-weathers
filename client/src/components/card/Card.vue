<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title text-center">{{ title }}</h5>
      <p class="card-text text-center">{{ date }}</p>
    </div>
    <p v-html="data.img"></p>
    <div class="card-body">
      <h5 class="card-title text-center">{{ data.desc }}</h5>
      <div class="card-text text-center">
        <strong>Nhiệt độ: {{ data.celsius }}</strong>
      </div>
      <div class="card-text text-center">{{ data.high }}</div>
      <div class="card-text text-center">{{ data.low }}</div>
    </div>
    <div class="card-footer text-center">
      <small class="text-muted">{{ data.updated }}</small>
    </div>
  </div>
</template>

<script>
export default {
  props: ["data"],
  data() {
    return {
      title: this.data.day.slice(0, this.data.day.length - 10),
      date: this.data.day.slice(-10, this.data.day.length)
    };
  }
};
</script>

<style>
</style>