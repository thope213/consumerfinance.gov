import { chartView } from '../views/chart-view.js';
import { expensesView } from '../views/expenses-view.js';
import { financialView } from '../views/financial-view.js';
import { navigationView } from '../views/navigation-view.js';
import { schoolView } from '../views/school-view.js';

const updateExpensesView = () => {
  expensesView.updateExpensesView();
};

const updateFinancialView = () => {
  financialView.updateFinancialItems();
};

const updateCostOfBorrowingChart = () => {
  chartView.updateCostOfBorrowingChart();
};

const updateMakePlanChart = () => {
  chartView.updateMakePlanChart();
};

const updateMaxDebtChart = () => {
  chartView.updateMaxDebtChart();
};

const updateAffordingChart = () => {
  chartView.updateAffordingChart();
};

const updateGradMeterChart = () => {
  chartView.updateGradMeterChart();
};

const updateRepaymentMeterChart = () => {
  chartView.updateRepaymentMeterChart();
};

const updateNavigationView = () => {
  navigationView.updateView();
}

export {
  updateExpensesView,
  updateFinancialView,
  updateCostOfBorrowingChart,
  updateMakePlanChart,
  updateMaxDebtChart,
  updateAffordingChart,
  updateGradMeterChart,
  updateRepaymentMeterChart,
  updateNavigationView
};
