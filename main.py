structure = {
    "1_Introduction": [
        "1.1_Mathematical_Formulation",
        "1.2_Example:_A_Transportation_Problem",
        "1.3_Continuous_versus_Discrete_Optimization",
        "1.4_Constrained_and_Unconstrained_Optimization",
        "1.5_Global_and_Local_Optimization",
        "1.6_Stochastic_and_Deterministic_Optimization",
        "1.7_Convexity",
        "1.8_Optimization_Algorithms",
        "1.9_Notes_and_References"
    ],
    "2_Fundamentals_of_Unconstrained_Optimization": [
        {
            "2.1_What_Is_a_Solution": [
                "2.1.1_Recognizing_a_Local_Minimum",
                "2.1.2_Nonsmooth_Problems"
            ]
        },
        {
            "2.2_Overview_of_Algorithms": [
                "2.2.1_Two_Strategies:_Line_Search_and_Trust_Region",
                "2.2.2_Search_Directions_for_Line_Search_Methods",
                "2.2.3_Models_for_Trust-Region_Methods",
                "2.2.4_Scaling"
            ]
        },
    ],
    "3_Line_Search_Methods": [
        {
            "3.1_Step_Length": [
                "3.1.1_The_Wolfe_Conditions",
                "3.1.2_The_Goldstein_Conditions",
                "3.1.3_Sufficient_Decrease_and_Backtracking"
            ]
        },
        "3.2_Convergence_of_Line_Search_Methods",
        {
            "3.3_Rate_of_Convergence": [
                "3.3.1_Convergence_Rate_of_Steepest_Descent",
                "3.3.2_Newton’s_Method",
                "3.3.3_Quasi-Newton_Methods"
            ]
        },
        {
            "3.4_Newton’s_Method_with_Hessian_Modification": [
                "3.4.1_Eigenvalue_Modification",
                "3.4.2_Adding_a_Multiple_of_the_Identity",
                "3.4.3_Modified_Cholesky_Factorization",
                "3.4.4_Modified_Symmetric_Indefinite_Factorization"
            ]
        },
        {
            "3.5_Step-Length_Selection_Algorithms": [
                "3.5.1_Interpolation",
                "3.5.2_Initial_Step_Length",
                "3.5.3_A_Line_Search_Algorithm_for_the_Wolfe_Conditions"
            ]
        },
        "3.6_Notes_and_References",
    ],
    "4_Trust-Region_Methods": [
        "4.1_Outline_of_the_Trust-Region_Approach",
        {
            "4.2_Algorithms_Based_on_the_Cauchy_Point": [
                "4.2.1_The_Cauchy_Point",
                "4.2.2_Improving_on_the_Cauchy_Point",
                "4.2.3_The_Dogleg_Method",
                "4.2.4_Two-Dimensional_Subspace_Minimization"
            ]
        },
        {
            "4.3_Global_Convergence": [
                "4.3.1_Reduction_Obtained_by_the_Cauchy_Point",
                "4.3.2_Convergence_to_Stationary_Points"
            ]
        },
        {
            "4.4_Iterative_Solution_of_the_Subproblem": [
                "4.4.1_The_Hard_Case",
                "4.4.2_Proof_of_Theorem_4.1",
                "4.4.3_Convergence_of_Algorithms_Based_on_Nearly_Exact_Solutions"
            ]
        },
        "4.5_Local_Convergence_of_Trust-Region_Newton_Methods",
        {
            "4.6_Other_Enhancements": [
                "4.6.1_Scaling",
                "4.6.2_Trust_Regions_in_Other_Norms"
            ]
        },
        "4.7_Notes_and_References",
    ],
    "5_Conjugate_Gradient_Methods": [
        {
            "5.1_The_Linear_Conjugate_Gradient_Method": [
                "5.1.1_Conjugate_Direction_Methods",
                "5.1.2_Basic_Properties_of_the_Conjugate_Gradient_Method",
                "5.1.3_A_Practical_Form_of_the_Conjugate_Gradient_Method",
                "5.1.4_Rate_of_Convergence",
                "5.1.5_Preconditioning",
                "5.1.6_Practical_Preconditioners"
            ]
        },
        {
            "5.2_Nonlinear_Conjugate_Gradient_Methods": [
                "5.2.1_The_Fletcher–Reeves_Method",
                "5.2.2_The_Polak–Ribière_Method_and_Variants",
                "5.2.3_Quadratic_Termination_and_Restarts",
                "5.2.4_Behavior_of_the_Fletcher–Reeves_Method",
                "5.2.5_Global_Convergence",
                "5.2.6_Numerical_Performance"
            ]
        },
        "5.3_Notes_and_References",
    ],
    "6_Quasi-Newton_Methods": [
        {
            "6.1_The_BFGS_Method": [
                "6.1.1_Properties_of_the_BFGS_Method",
                "6.1.2_Implementation"
            ]
        },
        {
            "6.2_The_SR1_Method": [
                "6.2.1_Properties_of_SR1_Updating"
            ]
        },
        "6.3_The_Broyden_Class",
        {
            "6.4_Convergence_Analysis": [
                "6.4.1_Global_Convergence_of_the_BFGS_Method",
                "6.4.2_Superlinear_Convergence_of_the_BFGS_Method",
                "6.4.3_Convergence_Analysis_of_the_SR1_Method"
            ]
        },
        "6.5_Notes_and_References",
    ],
    "7_Large-Scale_Unconstrained_Optimization": [
        {
            "7.1_Inexact_Newton_Methods": [
                "7.1.1_Local_Convergence_of_Inexact_Newton_Methods",
                "7.1.2_Line_Search_Newton–CG_Method",
                "7.1.3_Trust-Region_Newton–CG_Method",
                "7.1.4_Preconditioning_the_Trust-Region_Newton–CG_Method",
                "7.1.5_Trust-Region_Newton–Lanczos_Method"
            ]
        },
        {
            "7.2_Limited-Memory_Quasi-Newton_Methods": [
                "7.2.1_Limited-Memory_BFGS",
                "7.2.2_Relationship_with_Conjugate_Gradient_Methods",
                "7.2.3_General_Limited-Memory_Updating",
                "7.2.4_Compact_Representation_of_BFGS_Updating",
                "7.2.5_Unrolling_the_Update"
            ]
        },
        "7.3_Sparse_Quasi-Newton_Updates",
        "7.4_Algorithms_for_Partially_Separable_Functions",
        "7.5_Perspectives_and_Software",
        "7.6_Notes_and_References",
    ],
    "8_Calculating_Derivatives": [
        {
            "8.1_Finite-Difference_Derivative_Approximations": [
                "8.1.1_Approximating_the_Gradient",
                "8.1.2_Approximating_a_Sparse_Jacobian",
                "8.1.3_Approximating_the_Hessian",
                "8.1.4_Approximating_a_Sparse_Hessian"
            ]
        },
        {
            "8.2_Automatic_Differentiation": [
                "8.2.1_An_Example",
                "8.2.2_The_Forward_Mode",
                "8.2.3_The_Reverse_Mode",
                "8.2.4_Vector_Functions_and_Partial_Separability",
                "8.2.5_Calculating_Jacobians_of_Vector_Functions",
                "8.2.6_Calculating_Hessians:_Forward_Mode",
                "8.2.7_Calculating_Hessians:_Reverse_Mode",
                "8.2.8_Current_Limitations"
            ]
        },
        "8.3_Notes_and_References",
    ],
    "9_Derivative-Free_Optimization": [
        "9.1_Finite-Differences_and_Noise",
        {
            "9.2_Model-Based_Methods": [
                "9_2_1_Interpolation_and_Polynomial_Bases",
                "9_2_2_Updating_the_Interpolation_Set",
                "9_2_3_A_Method_Based_on_Minimum-Change_Updating"
            ]
        },
        {
            "9.3_Coordinate_and_Pattern-Search_Methods": [
                "9.3.1_Coordinate_Search_Method",
                "9.3.2_Pattern-Search_Methods"
            ]
        },
        "9.4_A_Conjugate-Direction_Method",
        "9.5_Nelder–Mead_Method",
        "9.6_Implicit_Filtering",
        "9.7_Notes_and_References",
    ],
    "10_Least-Squares_Problems": [
        "10.1_Background",
        "10.2_Linear_Least-Squares_Problems",
        {
            "10.3_Algorithms_for_Nonlinear_Least-Squares_Problems": [
                "10.3.1_The_Gauss–Newton_Method",
                "10.3.2_Convergence_of_the_Gauss–Newton_Method",
                "10.3.3_The_Levenberg–Marquardt_Method",
                "10.3.4_Implementation_of_the_Levenberg–Marquardt_Method",
                "10.3.5_Convergence_of_the_Levenberg–Marquardt_Method",
                "10.3.6_Methods_for_Large-Residual_Problems"
            ]
        },
        "10.4_Orthogonal_Distance_Regression",
        "10.5_Notes_and_References",
    ],
    "11_Nonlinear_Equations": [
        {
            "11.1_Local_Algorithms": [
                "11.1.1_Newton’s_Method_for_Nonlinear_Equations",
                "11.1.2_Inexact_Newton_Methods",
                "11.1.3_Broyden’s_Method",
                "11.1.4_Tensor_Methods"
            ]
        },
        {
            "11.2_Practical_Methods": [
                "11.2.1_Merit_Functions",
                "11.2.2_Line_Search_Methods",
                "11.2.3_Trust-Region_Methods"
            ]
        },
        {
            "11.3_Continuation_Homotopy_Methods": [
                "11.3.1_Motivation",
                "11.3.2_Practical_Continuation_Methods"
            ]
        },
        "11.4_Notes_and_References",
    ],
    "12_Theory_of_Constrained_Optimization": [
        "12.1_Local_and_Global_Solutions",
        "12.2_Smoothness",
        {
            "12.3_Examples": [
                "12.3.1_A_Single_Equality_Constraint",
                "12.3.2_A_Single_Inequality_Constraint",
                "12.3.3_Two_Inequality_Constraints"
            ]
        },
        "12.4_Tangent_Cone_and_Constraint_Qualifications",
        {
            "12.5_First-Order_Optimality_Conditions": [
                "12.5.1_First-Order_Optimality_Conditions_Proof",
                "12.5.1.1_Relating_the_Tangent_Cone_and_the_First-Order_Feasible_Direction_Set",
                "12.5.1.2_A_Fundamental_Necessary_Condition",
                "12.5.1.3_Farkas’_Lemma",
                "12.5.1.4_Proof_of_Theorem_12.1"
            ]
        },
        {
            "12.6_Second-Order_Conditions": [
                "12.6.1_Second-Order_Conditions_and_Projected_Hessians"
            ]
        },
        "12.7_Other_Constraint_Qualifications",
        "12.8_A_Geometric_Viewpoint",
        "12.9_Lagrange_Multipliers_and_Sensitivity",
        "12.10_Duality",
        "12.11_Notes_and_References",
    ],
    "13_Linear_Programming:_The_Simplex_Method": [
        "13.1_Linear_Programming",
        {
            "13.2_Optimality_and_Duality": [
                "13.2.1_Optimality_Conditions",
                "13_2_2_The_Dual_Problem"
            ]
        },
        {
            "13.3_Geometry_of_the_Feasible_Set": [
                "13.3.1_Bases_and_Basic_Feasible_Points",
                "13.3.2_Vertices_of_the_Feasible_Polytope"
            ]
        },
        {
            "13.4_The_Simplex_Method": [
                "13.4.1_Outline",
                "13.4.2_A_Single_Step_of_the_Method"
            ]
        },
        "13.5_Linear_Algebra_in_the_Simplex_Method",
        {
            "13.6_Other_Important_Details": [
                "13.6.1_Pricing_and_Selection_of_the_Entering_Index",
                "13.6.2_Starting_the_Simplex_Method",
                "13.6.3_Degenerate_Steps_and_Cycling"
            ]
        },
        "13.7_The_Dual_Simplex_Method",
        "13.8_Presolving",
        "13.9_Where_Does_the_Simplex_Method_Fit?",
        "13.10_Notes_and_References",
    ],
    "14_Linear_Programming:_Interior-Point_Methods": [
        {
            "14.1_Primal-Dual_Methods": [
                "14.1.1_Outline",
                "14.1.2_The_Central_Path",
                "14.1.3_Central_Path_Neighborhoods_and_Path-Following_Methods"
            ]
        },
        {
            "14.2_Practical_Primal-Dual_Algorithms": [
                "14.2.1_Corrector_and_Centering_Steps",
                "14.2.2_Step_Lengths",
                "14.2.3_Starting_Point",
                "14.2.4_A_Practical_Algorithm",
                "14.2.5_Solving_the_Linear_Systems"
            ]
        },
        {
            "14.3_Other_Primal-Dual_Algorithms_and_Extensions": [
                "14.3.1_Other_Path-Following_Methods",
                "14.3.2_Potential-Reduction_Methods",
                "14.3.3_Extensions"
            ]
        },
        "14.4_Perspectives_and_Software",
        "14.5_Notes_and_References",
    ],
    "15_Fundamentals_of_Algorithms_for_Nonlinear_Constrained_Optimization": [
        "15.1_Categorizing_Optimization_Algorithms",
        "15.2_The_Combinatorial_Difficulty_of_Inequality-Constrained_Problems",
        {
            "15.3_Elimination_of_Variables": [
                "15.3.1_Simple_Elimination_using_Linear_Constraints",
                "15.3.2_General_Reduction_Strategies_for_Linear_Constraints",
                "15.3.3_Effect_of_Inequality_Constraints"
            ]
        },
        {
            "15.4_Merit_Functions_and_Filters": [
                "15.4.1_Merit_Functions",
                "15.4.2_Filters"
            ]
        },
        "15.5_The_Maratos_Effect",
        {
            "15.6_Second-Order_Correction_and_Nonmonotone_Techniques": [
                "15.6.1_Nonmonotone_(Watchdog)_Strategy"
            ]
        },
        "15.7_Notes_and_References",
    ],
    "16_Quadratic_Programming": [
        {
            "16.1_Equality-Constrained_Quadratic_Programs": [
                "16.1.1_Properties_of_Equality-Constrained_QPs"
            ]
        },
        {
            "16.2_Direct_Solution_of_the_KKT_System": [
                "16.2.1_Factoring_the_Full_KKT_System",
                "16.2.2_Schur-Complement_Method",
                "16.2.3_Null-Space_Method"
            ]
        },
        {
            "16.3_Iterative_Solution_of_the_KKT_System": [
                "16.3.1_CG_Applied_to_the_Reduced_System",
                "16.3.2_The_Projected_CG_Method"
            ]
        },
        {
            "16.4_Inequality-Constrained_Problems": [
                "16.4.1_Optimality_Conditions_for_Inequality-Constrained_Problems",
                "16.4.2_Degeneracy"
            ]
        },
        {
            "16.5_Active-Set_Methods_for_Convex_QPs": [
                "16.5.1_Specification_of_the_Active-Set_Method_for_Convex_QPs",
                "16.5.2_Further_Remarks_on_the_Active-Set_Method",
                "16.5.3_Finite_Termination_of_Active-Set_Algorithm_on_Strictly_Convex_QPs",
                "16.5.4_Updating_Factorizations"
            ]
        },
        {
            "16.6_Interior-Point_Methods": [
                "16.6.1_Solving_the_Primal-Dual_System",
                "16.6.2_Step_Length_Selection",
                "16.6.3_A_Practical_Primal-Dual_Method"
            ]
        },
        {
            "16.7_The_Gradient_Projection_Method": [
                "16.7.1_Cauchy_Point_Computation",
                "16.7.2_Subspace_Minimization"
            ]
        },
        "16.8_Perspectives_and_Software",
        "16.9_Notes_and_References",
    ],
    "17_Penalty_and_Augmented_Lagrangian_Methods": [
        {
            "17.1_The_Quadratic_Penalty_Method": [
                "17.1.1_Motivation",
                "17.1.2_Algorithmic_Framework",
                "17.1.3_Convergence_of_the_Quadratic_Penalty_Method",
                "17.1.4_Ill_Conditioning_and_Reformulations"
            ]
        },
        {
            "17.2_Nonsmooth_Penalty_Functions": [
                "17.2.1_A_Practical_L1_Penalty_Method",
                "17.2.2_A_General_Class_of_Nonsmooth_Penalty_Methods"
            ]
        },
        {
            "17.3_Augmented_Lagrangian_Method:_Equality_Constraints": [
                "17.3.1_Motivation_and_Algorithmic_Framework",
                "17.3.2_Properties_of_the_Augmented_Lagrangian"
            ]
        },
        {
            "17.4_Practical_Augmented_Lagrangian_Methods": [
                "17.4.1_Bound-Constrained_Formulation",
                "17.4.2_Linearly_Constrained_Formulation",
                "17.4.3_Unconstrained_Formulation"
            ]
        },
        "17.5_Perspectives_and_Software",
        "17.6_Notes_and_References",
    ],
    "18_Sequential_Quadratic_Programming": [
        {
            "18.1_Local_SQP_Method": [
                "18.1.1_SQP_Framework",
                "18.1.2_Inequality_Constraints"
            ]
        },
        {
            "18.2_Preview_of_Practical_SQP_Methods": [
                "18.2.1_IQP_and_EQP",
                "18.2.2_Enforcing_Convergence"
            ]
        },
        {
            "18.3_Algorithmic_Development": [
                "18.3.1_Handling_Inconsistent_Linearizations",
                "18.3.2_Full_Quasi-Newton_Approximations",
                "18.3.3_Reduced-Hessian_Quasi-Newton_Approximations",
                "18.3.4_Merit_Functions",
                "18.3.5_Second-Order_Correction"
            ]
        },
        "18.4_A_Practical_Line_Search_SQP_Method",
        {
            "18.5_Trust-Region_SQP_Methods": [
                "18.5.1_A_Relaxation_Method_for_Equality-Constrained_Optimization",
                "18.5.2_SQP_(Sequential_L1_Quadratic_Programming)",
                "18.5.3_Sequential_Linear-Quadratic_Programming_(SLQP)",
                "18.5.4_A_Technique_for_Updating_the_Penalty_Parameter"
            ]
        },
        "18.6_Nonlinear_Gradient_Projection",
        {
            "18.7_Convergence_Analysis": [
                "18.7.1_Rate_of_Convergence"
            ]
        },
        "18.8_Perspectives_and_Software",
        "18.9_Notes_and_References",
    ],
    "19_Interior-Point_Methods_for_Nonlinear_Programming": [
        "19.1_Two_Interpretations",
        "19.2_A_Basic_Interior-Point_Algorithm",
        {
            "19.3_Algorithmic_Development": [
                "19.3.1_Primal_vs._Primal-Dual_System",
                "19.3.2_Solving_the_Primal-Dual_System",
                "19.3.3_Updating_the_Barrier_Parameter",
                "19.3.4_Handling_Nonconvexity_and_Singularity",
                "19.3.5_Step_Acceptance:_Merit_Functions_and_Filters",
                "19.3.6_Quasi-Newton_Approximations",
                "19.3.7_Feasible_Interior-Point_Methods"
            ]
        },
        "19.4_A_Line_Search_Interior-Point_Method",
        {
            "19.5_A_Trust-Region_Interior-Point_Method": [
                "19.5.1_An_Algorithm_for_Solving_the_Barrier_Problem",
                "19.5.2_Step_Computation",
                "19.5.3_Lagrange_Multipliers_Estimates_and_Step_Acceptance",
                "19.5.4_Description_of_a_Trust-Region_Interior-Point_Method"
            ]
        },
        "19.6_The_Primal_Log-Barrier_Method",
        {
            "19.7_Global_Convergence_Properties": [
                "19.7.1_Failure_of_the_Line_Search_Approach",
                "19.7.2_Modified_Line_Search_Methods",
                "19.7.3_Global_Convergence_of_the_Trust-Region_Approach"
            ]
        },
        "19.8_Superlinear_Convergence",
        "19.9_Perspectives_and_Software",
        "19.10_Notes_and_References",
    ],
    "A_Background_Material": [
        {
            "A.1_Elements_of_Linear_Algebra": [
                "A.1.1_Vectors_and_Matrices",
                "A.1.2_Norms",
                "A.1.3_Subspaces",
                "A.1.4_Eigenvalues,_Eigenvectors,_and_the_Singular-Value_Decomposition",
                "A.1.5_Determinant_and_Trace",
                "A.1.6_Matrix_Factorizations:_Cholesky,_LU,_QR",
                "A.1.7_Symmetric_Indefinite_Factorization",
                "A.1.8_Sherman–Morrison–Woodbury_Formula",
                "A.1.9_Interlacing_Eigenvalue_Theorem",
                "A.1.10_Error_Analysis_and_Floating-Point_Arithmetic",
                "A.1.11_Conditioning_and_Stability"
            ]
        },
        {
            "A.2_Elements_of_Analysis,_Geometry,_Topology": [
                "A.2.1_Sequences",
                "A.2.2_Rates_of_Convergence",
                "A.2.3_Topology_of_the_Euclidean_Space_IRn",
                "A.2.4_Convex_Sets_in_IRn",
                "A.2.5_Continuity_and_Limits",
                "A.2.6_Derivatives",
                "A.2.7_Directional_Derivatives",
                "A.2.8_Mean_Value_Theorem",
                "A.2.9_Implicit_Function_Theorem",
                "A.2.10_Order_Notation",
                "A.2.11_Root-Finding_for_Scalar_Equations"
            ]
        }
    ]
}

import os
from typing import Dict, Any

def create_directories_and_files(
        base_path: str, 
        structure: Dict[str, Any], 
        readme_file, 
        parent_path: str = "", 
        level: int = 1
    ):
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("/", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {item}\n\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
                    
                    
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {item}\n\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.md)\n")
        else:
            # 创建文件并写入初始内容
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {key}\n\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")
            
            
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {key}\n\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# Numerical Optimization\n\n")
        readme_file.write("这是一个关于Numerical Optimization的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()