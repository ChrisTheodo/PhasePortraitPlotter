import numpy as np
import matplotlib.pyplot as plt

def phase_portrait(A, x_range=(-2, 2), y_range=(-2, 2), n_grid=20):
    
    x = np.linspace(*x_range, n_grid)
    y = np.linspace(*y_range, n_grid)
    X, Y = np.meshgrid(x, y)
    
    U = A[0,0]*X + A[0,1]*Y
    V = A[1,0]*X + A[1,1]*Y

    plt.figure(figsize=(6,6))
    plt.quiver(X, Y, U, V, color="blue", angles="xy", scale=20, scale_units="xy", width=0.004)

    
    t = np.linspace(0, 2, 100)
    initials = [(1,1), (-1,1), (1,-1), (-1,-1), (0.5,0), (0,1)]
    for x0, y0 in initials:
        xs = x0 * np.exp(A[0,0]*t) if A[0,1] == 0 and A[1,0] == 0 else None
        ys = y0 * np.exp(A[1,1]*t) if A[0,1] == 0 and A[1,0] == 0 else None
        
        if xs is None:
            continue  
        plt.plot(xs, ys, lw=2)

    # idiodianysmata
    eigvals, eigvecs = np.linalg.eig(A)

    for i in range(len(eigvals)):
        v = eigvecs[:, i]

        plt.plot([0, v[0]], [0, v[1]], color="red", lw=2, label=f"eig {i+1}")
        plt.plot([0, -v[0]], [0, -v[1]], color="red", lw=2)  # και στην αντίθετη κατεύθυνση

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.title(f"πορτραατο φασης για A=\n{A}")
    plt.show()


A = np.array([[3, -13],
              [5, 1]])

phase_portrait(A)
