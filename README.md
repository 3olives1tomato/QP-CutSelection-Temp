# QP-CutSelection-Temp

Low dimensional, data-driven, cut selection for nonconvex QP solvers, using linear outer-approximations SDP relaxations.

This project is a modified version of [SDPCutSel-via-NN](https://github.com/rb2309/SDPCutSel-via-NN) covered by the GNU General Public License version 3.0.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

---

## Code Organization

### Python Files

- **`CutSolver_TemporalSets.py`**: QP solver class to implement temporal-sets in the selection and replacements of low-dimensional cuts 
- **`Run_qp_solver.py`**: File to run the QP solver on the BoxQP instances and save the results
- **`utilities.py`**: Implements data sampling (Section 4) for training and testing neural networks and the examples in Fig 1, 3-6, and times reported in Table 2 for NN/Mosek

### Folders

- **`boxqp_instances`**: All BoxQP instances (together with solutions) and the powerflow instance used
- **`neural_nets`**: The trained neural nets used in the solvers/manuscript results as Matlab functions (2-5 dimensional) and compiled Win/Linux C libraries (NNs.dll/so), the Matlab Coder projects to compile them and Matlab checkpoint files to continue training them (from current parameters on any data), and training script 'train_NNs.m' (well-documented) which can use existing/new data to continue/start training
