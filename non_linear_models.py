import numpy as np
import model_LMM


def nl_models_new(x, E):
    # Model settings
    P_min = -100
    b_min = -100
    b_max = 100
    m0 = np.cos(np.pi/4)
    m = 1

    # Optimizer settings
    options = {'disp': False, 'algorithm': 'sqp', 'maxiter': 50000, 'ftol': 1e-10, 'gtol': 1e-8}

    d, N = x.shape
    _, p = E.shape

    # Linear unmixing
    a_LMM = np.zeros((p, N))
    x_LMM = np.zeros((d, N))
    for i in range(N):
        a_ini = np.ones(p)/p
        a_LMM[:, i] = fmincon(lambda a: np.sum((x[:, i] - model_LMM.model_LMM(a, E))**2), a_ini, [], [], np.ones((1, p)), 1, np.zeros(p), np.ones(p), options=options)
        x_LMM[:, i] = model_LMM.model_LMM(a_LMM[:, i], E)

    # # Unmixing with Fan model
    # a_FM = np.zeros((p, N))
    # x_FM = np.zeros((d, N))
    # for i in range(N):
    #     a_ini = a_LMM[:, i]
    #     a_FM[:, i] = fmincon(lambda a: np.sum((x[:, i] - model_FM(a, E))**2), a_ini, [], [], np.ones((1, p)), 1, np.zeros(p), np.ones(p), options=options)
    #     x_FM[:, i] = model_FM(a_FM[:, i], E)

    # # Unmixing with generalized bilinear model
    # a_GBM = np.zeros((p + int(p*(p-1)/2), N))
    # x_GBM = np.zeros((d, N))
    # for i in range(N):
    #     a_ini = np.concatenate((a_LMM[:, i], np.zeros(int(p*(p-1)/2))))
    #     a_GBM[:, i] = fmincon(lambda a: np.sum((x[:, i] - model_GBM(a, E))**2), a_ini, [], [], np.concatenate((np.ones(p), np.zeros(int(p*(p-1)/2)))), 1, np.zeros(p + int(p*(p-1)/2)), np.ones(p + int(p*(p-1)/2)), options=options)
    #     x_GBM[:, i] = model_GBM(a_GBM[:, i], E)

    # # Unmixing with PPNM model
    # a_PPNM = np.zeros((p + 1, N))
    # x_PPNM = np.zeros((d, N))
    # for i in range(N):
    #     a_ini = np.concatenate((a_LMM[:, i], [0]))
    #     a_PPNM[:, i] = fmincon(lambda a: np.sum((x[:, i] - model_PPNM(a, E))**2), a_ini, [], [], np.concatenate((np.ones(p), [0])), 1, np.concatenate((np.zeros(p), [b_min])), np.concatenate((np.ones(p), [b_max])), options=options)
    #     x_PPNM[:, i] = model_PPNM(a_PPNM[:, i], E)

    # # Unmixing with MLM model
    # a_MLM = np.zeros((p + 1, N))
    # x_MLM = np.zeros((d, N))
    # for i in range(N):
    #     a_ini = np.concatenate((a_LMM[:, i], [0.0]))
    #     a_MLM[:, i] = fmincon(lambda a: np.sum((x[:, i] - model_MLM(a, E))**2), a_ini, [], [], np.concatenate((np.ones(p), [0])), 1, np.concatenate((np.zeros(p), [P_min])), np.ones(p + 1), options=options)
    #     x_MLM[:, i] = model_MLM(a_MLM[:, i], E)

    # # Unmixing with Hapke model
    # w = (((m0 + m)**2)*(E**2) + (1 + 4*m*m0*E)*(1 - E))**0.5 - (m0 + m)*E
    # w = w/(1 + 4*m*m0*E)
    # w = 1 - w**2

    # y = (((m0 + m)**2)*(x**2) + (1 + 4*m*m0*x)*(1 - x))**0.5 - (m0 + m)*x
    # y = y/(1 + 4*m*m0*x)
    # y = 1 - y**2

    # a_hap = np.zeros((p, N))
    # x_hap = np.zeros((d, N))
    # for i in range(N):
    #     a_ini = np.ones(p)/p
    #     a_hap[:, i] = fmincon(lambda a: np.sum((y[:, i] - model_LMM(a, w))**2), a_ini, [], [], np.ones((1, p)), 1, np.zeros(p), np.ones(p), options=options)
    #     x_hap[:, i] = model_LMM(a_hap[:, i], w)

    # x_hap = x_hap/((1 + 2*m*(1 - x_hap)**0.5)*(1 + 2*m0*(1 - x_hap)**0.5))

    # return a_LMM, x_LMM, a_FM, x_FM, a_GBM, x_GBM, a_PPNM, x_PPNM, a_MLM, x_MLM, a_hap, x_hap

    return a_LMM, x_LMM