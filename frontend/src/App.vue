<script setup>
fetch("https://fakeradmin.zeabur.app/")
  .then(res => res.json())
  .then(data => console.log(data))
</script>

<template>
<h1>Faker Admin</h1>
</template>

<style scoped>

</style>
