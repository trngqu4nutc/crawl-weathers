<template>
  <tr>
    <th scope="row">{{ day.day }}</th>
    <td style="width: 10" v-html="day.img"></td>
    <td>{{ day.desc }}</td>
    <td>{{ day.celsius }}</td>
    <td>{{ day.high }}</td>
    <td>{{ day.low }}</td>
  </tr>
</template>
<script>
export default {
  props: ["day"]
};
</script>

<style>
</style>