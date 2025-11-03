<script setup>
const props = defineProps(["currentPage", "total", "pageSize"]);
const currentPage = defineModel('currentPage')
</script>

<template>
  <el-row justify="center">
    <el-pagination
      v-model:current-page="currentPage"
      :current-page="currentPage"
      :total="total"
      :page-size="pageSize"
      layout="prev, pager, next" />
  </el-row>
</template>
