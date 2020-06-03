<template>
  <div>
    <Header />
    <div class="container">
      <transition name="slide">
        <router-view />
      </transition>
    </div>
  </div>
</template>

<script>
import Header from "./components/layouts/Header";
export default {
  components: {
    Header
  }
};
</script>

<style>
body {
  background: url("https://images.pexels.com/photos/1450360/pexels-photo-1450360.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940")
    no-repeat;
  /* background-image: linear-gradient(to right, red , blue); */
  background-size: cover;
}
.card {
  opacity: 0.8;
}
.text-title {
  color: #caf8ea;
}
.card:hover {
  opacity: 1;
  background-color: white;
  /* color: #4ed8e2; */
  transition: 0.5s;
}
.slide-enter {
  opacity: 0;
}
.slide-enter-active {
  transition: opacity 0.7s;
  animation: slide-in 0.5s ease-out forwards;
  transform: translateX(0);
}
/* .slide-leave{
    opacity: 1;
  }
  .slide-leave-active{
    transition: opacity .7s;
    animation: slide-out .5s ease-out forwards;
  } */
@keyframes slide-in {
  0% {
    transform: translateX(-100px);
  }
  100% {
    transform: translateX(0);
  }
}
@keyframes slide-out {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(100px);
  }
}
</style>
