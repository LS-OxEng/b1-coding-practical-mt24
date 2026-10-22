# Discrete Proportional-Derivative Controller for UUV depth regulation  

class PDController:

# The __init_ method initialises the controller with proportional (Kp) and derivative (Kd) gains, and sets the previous error to zero.
    def __init__(self, Kp=0.15, Kd=0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0


# The __call__ method allows the controller to be used as a callable object, taking the reference and observation as inputs and returning the computed action via the PD control law. It calculates the error, computes the action based on the proportional and derivative terms, and updates the previous error for the next call.
    def __call__(self, reference: float, observation: float) -> float:
        error = reference - observation

        action = (self.Kp * error + self.Kd * (error - self.previous_error))

        self.previous_error = error
        return action

# Controller memory reset to clear previous error prior to a new simulation or test
    def reset(self):
        self.previous_error = 0.0