1. What is Python SciPy?
   * SciPy is a Python library used to solve scientific and mathematical problems
   * Built on NumPy
   * Allows manipulation and visualizing

2. NumPy vs SciPy
   * NumPy and SciPy used for mathematical and numerical analysis
   * NumPy contains array data and basic operations
   * SciPy consists of all the numerical code
   * SciPy contains fully-featured versions of mathematical and scientific functions

3. Sub-Packages in SciPy
   | Name | Description |
   | ---- | ----------- |
   | cluster | Clustering algorithms |
   | constants | Physical and mathematical constants |
   | fftpack | Fast Fourier Transform routines |
   | integrate | Integration and ordinary differential equation solvers |
   | interpolate | Interpolation and smoothing splines |
   | io  |  Input and Output |
   | linalg | Linear algebra |
   | ndimage | N-dimensional image processing |
   | odr | Orthogonal distance regression |
   | optimize | Optimization and root-finding routines |
   | signal | Signal processing |
   | sparse | Sparse matrices and associated routines |
   | spatial | Spatial data structures and algorithms |
   | special | Special functions |
   | stats | Statistical distributions and functions |
   
4. Basic Functions
   * help() : Returns information about any function, keyword, class, etc
   * info() : Returns information about any function, keyword, class, etc
   * source() : Returns the source code only for objects written in Python

5. Special Functions
   * Functions available for Mathematical Physics
   * Some of these functions include gamma, beta, hypergeometric, parabolic cylinder, etc

6. Integration Functions
   * Integration deals with adding slices to datermine the whole. Integration can be used to fing displacement, area, etc.
   1. General Integration
      * The quad function calculates the integral of a function which has one variable.
   2. Double Integration
      * The dblquad function calculates double integral of a function which has two variables.
      
7. Fourier Transformations
   * Fourier analysis is a method that deals with expressing a function as a sum of periodic components and recovering the signal from those components
   * The fft and ifft functions can be used to return the discrete Fourier transform of a real or comples sequence.

8. Linear Algebra
   * SciPy is built on ATLAS LAPACK and BLAS libraries and is extremely fast in solving problems related to linear algebra
   * Inverse of a matrix A is the matrix B such that AB=I where I is the identity matrix consisting of ones down the main diagonal denoted as B=A⁻¹

9. Interpolation Functions
   * Interpolation refers to constructing new data points within a set of known data points. The scipy.interpolate consists of spline functions and classes, one-dimensional and multi-dimensional (univariate and multivariate) interpolation classes, etc.
