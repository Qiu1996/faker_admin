<script setup>
import { ORDER_STATUS, AMOUNT_RANGES } from "../constants.js"
const statusFilter = defineModel("statusFilter");
const inputFilter = defineModel("inputFilter");
const dateFilter = defineModel("dateFilter");
const amountFilter = defineModel("amountFilter");
</script>

<template>
<el-row :gutter="14">
    <el-col :span="6">
      <el-date-picker
        v-model="dateFilter"
        type="daterange"
        unlink-panels
        range-separator="|"
        start-placeholder="起始日期"
        end-placeholder="結束日期"
      />
    </el-col>
    <el-col :span="6">
      <el-select
        v-model="statusFilter"
        multiple
        collapse-tags
        collapse-tags-tooltip
        placeholder="選取付款狀態">
        <el-option
          v-for="(value, key) in ORDER_STATUS"
          :label="value" :value="key"/>
      </el-select>
    </el-col>
    <el-col :span="6">
      <el-input
        v-model="inputFilter"
        placeholder="輸入訂單編號或客戶姓名" />
    </el-col>
    <el-col :span="6">
      <el-select
        v-model="amountFilter"
        clearable
        placeholder="選取金額範圍">
        <el-option
          v-for="(_, key) in AMOUNT_RANGES"
          :label="key" :value="key" />
      </el-select>
    </el-col>
</el-row>

</template>

<style scoped>
:deep(.el-date-editor) {
    width: 100%;
}

:deep(.el-date-editor), :deep(.el-select > div), :deep(.el-input > div){
  height: 50px;
  box-sizing: border-box;
  font-size: 16px;
}

:deep(.el-date-editor > *){
  font-size: 16px;
}
</style>
