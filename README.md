# mathmod - библиотека программ для численного моделирования

 

## Содержание
- [mathmod - библиотека программ для численного моделирования](#mathmod---библиотека-программ-для-численного-моделирования)
  - [Содержание](#содержание)
  - [Решение систем линейных алгебраических уравнений (СЛАУ)](#решение-систем-линейных-алгебраических-уравнений-слау)
    - [Доступные методы](#доступные-методы)
  - [Решение нелинейных уравнений](#решение-нелинейных-уравнений)
    - [Доступные методы](#доступные-методы-1)
  - [Установка](#установка)

---

## Решение систем линейных алгебраических уравнений (СЛАУ)
Библиотека включает несколько методов для численного решения СЛАУ:


### Доступные методы
1. **Метод Гаусса-Зейделя**
   - Итерационный метод для решения СЛАУ с диагонально преобладающей матрицей.
   - **Функция:** `gauss_zeydel(A, b, epsilon=1e-6, norma=1)`
   - **Оценка погрешности:**

$$
\| x^{(k+1)} - x^{(k)} \|_1 \leq \varepsilon
$$

   где:
         <br><br>- $x^{(k)}$ — приближённое решение на $k$-й итерации;<br>
         <br>- $x^{(k + 1)}$ — приближённое решение на следующей итерации;<br>
         <br>- $|| \cdot ||_p$ — норма вектора, например, $p = 1$ или $\infty$ (по умолчанию единичная норма);<br>
         <br>- $\varepsilon$ — заданная точность (по умолчанию $10^{-6}$).

   ![Метод Зейделя](images/image.png)


1. **Метод Якоби**
   - Итерационный метод для решения СЛАУ.
   - Подходит для разреженных матриц.
   - **Функция:** `jacobi(A, b, epsilon=1e-6, norma=1)`

2. **Метод Холецкого (LLT-разложение)**
   - Для решения СЛАУ с симметрично положительно определённой матрицей.
   - **Функция:** `cholecky(A, b)`
   
3. **Метод LU-разложения**
   - Универсальный метод, подходящий для большинства задач.
   - **Функция:** `lu(A, b)`

4. **Метод Гаусса (схема единственного деления)**
   - Классический метод для решения СЛАУ путём прямого и обратного хода.
   - **Функция:** `gauss_single_division(A, b)`

---

## Решение нелинейных уравнений
Библиотека включает методы для численного решения нелинейных уравнений. Эти методы позволяют находить корни функций с различными подходами:

### Доступные методы
1. **Метод Ньютона (касательных)**
   - Быстрый итерационный метод для нахождения корня уравнения  $f(x) = 0$.
   - Требует предоставления функции $f(x)$ и её производной $f'(x)$.
   - **Функция:** `newton(f, df, x, eps=1e-6)`

2. **Упрощённый метод Ньютона**
   - Упрощённая версия метода Ньютона, где производная функции вычисляется только один раз.
   - **Функция:** `simplified_newton(f, df, x0, eps=1e-6)`

3. **Метод секущих**
   - Не требует аналитической производной функции.
   - Использует приближённую производную.
   - **Функция:** `secant(f, x__minus_1, x_n, eps=1e-6)`

4. **Метод ложного положения**
   - Работает на основе деления отрезка, учитывая значения функции.
   - Требует, чтобы начальный отрезок $[a, b]$ удовлетворял условию $f(a) * f(b) < 0$.
   - **Функция:** `false_position(f, a, b, eps=1e-6)`
---

## Установка
Для использования библиотеки склонируйте репозиторий и установите необходимые зависимости:
```bash
git clone https://github.com/BaranovSerV/mathmod.git
cd mathmod
pip install -r requirements.txt