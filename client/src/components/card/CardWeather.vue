<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title text-center">{{ data.day }}</h5>
    </div>
    <p v-html="data.img"></p>
    <div class="card-body">
      <h5 class="card-title text-center">{{ data.desc }}</h5>
        <div class="card-text text-center"><strong>Nhiệt độ: {{ data.celsius }}</strong></div>
        <div class="card-text text-center">{{ data.high }}</div>
        <div class="card-text text-center">{{ data.low }}</div>
     </div>
    <div class="card-footer">
      <small class="text-muted">{{ data.updated }}</small>
    </div>
  </div>
</template>

<script>
export default {
    props: ['data']
};
</script>

<style>
</style>