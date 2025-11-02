<script setup>
import { ref } from "vue";

const orders = ref([]);

const fetchOrdersData = async () => {
  const res = await fetch("https://fakeradmin.zeabur.app/");
  orders.value = await res.json();
};

fetchOrdersData();
</script>

<template>
<h1>Order List</h1>
<el-table :data="orders" style="width: 100%">
  <el-table-column prop="order_number" label="訂單編號" />
   <el-table-column prop="customer_name" label="客戶姓名" />
   <el-table-column prop="amount" label="訂單金額" />
   <el-table-column prop="status" label="付款狀態" />
   <el-table-column prop="created_at" label="訂單建立時間" />
</el-table>
</template>
