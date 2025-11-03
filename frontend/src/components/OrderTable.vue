<script setup>
const props = defineProps(["orders"]);
const emit = defineEmits(["sort-change"]);

</script>

<template>
<el-table
  @sort-change="$emit('sort-change', $event)"
  :data="orders" style="width: 100%">
  <el-table-column sortable="custom" prop="order_number" label="訂單編號" />
  <el-table-column sortable="custom" prop="customer_name" label="客戶姓名" />
  <el-table-column sortable="custom" prop="amount" label="訂單金額" />
  <el-table-column sortable="custom" prop="status" label="付款狀態" />
  <el-table-column sortable="custom" prop="created_at" label="訂單建立時間" />
</el-table>
</template>
