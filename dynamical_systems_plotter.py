import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_quiver(dx , dy , xlims=[-2.5,2.5] , ylims=[-2.5,2.5] , title="Dyn" , plot_xlims=[-3,3] , plot_ylims=[-3,3] , number_points = 20):
    '''
    Plot the vector field for a 2D system of differential equations/dynamical system
    
    ->Arguments:

    @dx,dy : Equation for dx/dt and dy/dt respectively, must be defined as lambda function

    ->Example:

    dx = lambda x,y: 3*x + 2*y
    dy = lambda x,y: x*y
    '''
    X , Y = np.meshgrid(np.linspace(*xlims , number_points),np.linspace(*ylims , number_points))
    t = 0 
    u = np.array(list(map(dx ,X,Y)))
    v = np.array(list(map(dy, X,Y)))
    fig = plt.figure(num=None, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')        
    plt.quiver(X,Y,u,v,color='blue')
    plt.xlim(plot_xlims)
    plt.ylim(plot_ylims)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.rcParams.update({'font.size': 22})
    plt.legend(loc=4)
    plt.title(title)
    plt.grid(True)
    return fig

from scipy.integrate import odeint

def dyn_sys(state,t,dx,dy):
    '''
    Applies dx and dy function to the current state of the system.

    -> Arguments:
	
    @state : Array containing the state of coordinate x and y
    '''
    return [dx(*state),dy(*state)]
def integrate_ode(sys,dx,dy,initial,t):
    '''
    Auxiliary function to use odeint from scipy within our framework
    
    -> Arguments:

    @sys: dyn_sys previously defined
    @initial: array with the initial conditions x_0 and y_0
    @t : array containing all the times coordinates which will be serve as domain for the integration
    '''
    return odeint(sys,initial,t,args=(dx,dy))


def phase_space_sol(dx,dy,t,number_solutions = 9,t_points=20 , title="Title",xlims=[-3,3] , ylims=[-3,3]  ,x_initial=[-1.5,1.5],y_initial=[-1.5,1.5] ,plot_xlims=[-3,3],plot_ylims=[-3,3],number_points = 20):
    
    '''
    -> Description:
	
	Plots the vector field along with different solutions for the system of ODE

    -> Arguments:

	@dx,dy = lambda functions governing the system, defined as in the first case
	@t = max time which will be used for integration
    '''
    tspan = np.linspace(0.1,t,t_points)
    x_0 = np.linspace(*x_initial , int(np.sqrt(number_solutions)))
    y_0 = np.linspace(*y_initial , int(np.sqrt(number_solutions)))
    solutions = np.array([integrate_ode(dyn_sys, dx,dy,[x_init,y_init],tspan)  for x_init in x_0 for y_init in y_0])
    fig = plot_quiver(dx , dy , title=title, xlims=xlims,ylims=ylims , plot_xlims=plot_xlims , plot_ylims=plot_ylims , number_points=number_points)
    for sol in solutions:
        plt.plot(sol[:,0], sol[:,1], 'r--',linewidth=4  , label="Traxectoria Solucion")
        plt.plot([sol[0,0]], [sol[0,1]] , 'or', markersize=15,markeredgewidth=1.5, markeredgecolor= "k", label="Punto Inicial") # start
        plt.plot([sol[-1,0]], [sol[-1,1]], 'sr',markersize=10,markeredgewidth=1.5, markeredgecolor="k" , label="Punto Final")
    plt.xlabel("X")
    plt.ylabel("Y")     
    legend_elements = [Line2D([0], [0], color='r', lw=4, label='Solution'),
                   Line2D([0], [0], marker='o', color='r', label='Iniital Point',
                          markerfacecolor='r', markersize=15,markeredgewidth=1.5, markeredgecolor= "k"),
                   Line2D([0], [0], marker='s', color='r', label='Final Point',
                          markerfacecolor='r', markersize=15,markeredgewidth=1.5, markeredgecolor= "k")]
    plt.legend(handles=legend_elements,loc=4,prop={'size': 15})
    
    return f
