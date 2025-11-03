<script setup>
import { ORDER_STATUS } from "../constants.js"
const props = defineProps(["orders"]);
const emit = defineEmits(["sort-change"]);

const formatStatus = (row) => ORDER_STATUS[row.status]
</script>

<template>
<el-table
  @sort-change="$emit('sort-change', $event)"
  :data="orders" style="width: 100%">
  <el-table-column sortable="custom" prop="order_number" label="訂單編號" />
  <el-table-column sortable="custom" prop="customer_name" label="客戶姓名" />
  <el-table-column sortable="custom" prop="amount" label="訂單金額" />
  <el-table-column sortable="custom" prop="status" label="付款狀態" :formatter="formatStatus" />
  <el-table-column sortable="custom" prop="created_at" label="訂單建立時間" />
</el-table>
</template>
