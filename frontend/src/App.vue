<script setup>
import { ref, computed } from "vue"
import { AMOUNT_RANGES } from "./constants.js"
import OrderTable from "./components/OrderTable.vue";
import Pagination from "./components/Pagination.vue"
import FilterBar from "./components/FilterBar.vue";

const orderList = ref([]);
const currentPage = ref(1);
const pageSize = ref(10);
const statusFilter = ref([]);
const inputFilter = ref();
const dateFilter = ref();
const amountFilter = ref();

const API_URL = import.meta.env.DEV
  ? 'http://localhost:8000'
  : 'https://fakeradmin.zeabur.app'

const fetchOrdersData = async () => {
  const res = await fetch(`${API_URL}/`);
  orderList.value = await res.json();
};
fetchOrdersData();

const filterOrders = computed(() => {
  let result = orderList.value

  // 狀態篩選
  if (statusFilter.value.length > 0) {
    result = result.filter(order =>
      statusFilter.value.includes(order.status)
    )
  }

  // 搜尋篩選
  if (inputFilter.value){
    result = result.filter(order =>
      order.order_number.includes(inputFilter.value) ||
      order.customer_name.includes(inputFilter.value)
    )
  }

  // 日期篩選
  if (dateFilter.value){
    result = result.filter(order => {
      const orderDate = new Date(order.created_at)
      const [startDate, endDate] = dateFilter.value
      return orderDate >= startDate && orderDate <=endDate
    }
    )
  }

  // 金額篩選
  if (amountFilter.value){
    result = result.filter(order => {
      const [minAmount, maxAmount] = AMOUNT_RANGES[amountFilter.value];
      return order.amount >= minAmount && order.amount <= maxAmount;
    })
  }


  return result
})


const displayOrders = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  const end = start + pageSize.value
  return filterOrders.value.slice(start, end)
})

const handleSort = ({ prop, order }) => {
  if (!order) {
    orderList.value.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    return;
  }

  const direction = order === "ascending" ? -1 : 1;

  const comparators = {
    order_number: (item1, item2) => item1.localeCompare(item2),
    customer_name: (item1, item2) => item1.localeCompare(item2, "zh-TW"),
    amount: (item1, item2) => item1 - item2,
    status: (item1, item2) => item1.localeCompare(item2),
    created_at: (item1, item2) => new Date(item1) - new Date(item2)
  };

  orderList.value.sort((item1, item2) =>
    comparators[prop](item1[prop], item2[prop]) * direction
  );
}

</script>

<template>
<h1>Order List</h1>
<FilterBar
  v-model:status-filter="statusFilter"
  v-model:input-filter="inputFilter"
  v-model:date-filter="dateFilter"
  v-model:amount-filter="amountFilter" />
<Pagination
  v-model:current-page="currentPage"
  :page-size=pageSize
  :total=filterOrders.length />
<OrderTable
  :orders=displayOrders
  @sort-change="handleSort"
  />
</template>
