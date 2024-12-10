pandoc READ.md -o Mathmod.pdf --pdf-engine=xelatex --toc -V mainfont="Times New Roman" -V toc-title="Содержание" -V fig_caption=false



$$
\begin{aligned}
    (n + 1)a_{0} + (\sum_{i = 0}^n x_i)a_{1} + (\sum_{i = 0}^n x_i^2)a_{2}  &= \sum_{i = 0}^n y_i, \\
    (\sum_{i = 0}^n x_i)a_{0} + (\sum_{i = 0}^n x_i^2)a_{1} + (\sum_{i = 0}^n x_i^3)a_{2} &= \sum_{i = 0}^n y_i x_i, \\
    (\sum_{i = 0}^n x_i^2)a_{0} + (\sum_{i = 0}^n x_i^3)a_{1} + (\sum_{i = 0}^n x_i^4)a_{2} &= \sum_{i = 0}^n y_i x_i^2, \\
\end{aligned}
$$
