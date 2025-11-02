<script setup>
const props = defineProps(["currentPage", "total", "pageSize"]);
const emit = defineEmits(["update:currentPage"]);

const handlePageChange = (page) => {
  emit('update:currentPage', page)
}
</script>

<template>
  <el-row justify="center">
    <el-pagination
      @current-change="handlePageChange"
      :current-page="currentPage"
      :total="total"
      :page-size="pageSize"
      layout="prev, pager, next" />
  </el-row>
</template>
