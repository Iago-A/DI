package com.example.aerocatalogo.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.aerocatalogo.repositories.UserRepository;

public class LoginViewModel extends ViewModel {
    private final MutableLiveData<String> errorMessage = new MutableLiveData<>();
    private final MutableLiveData<Boolean> isLoginSuccessful = new MutableLiveData<>();
    private final UserRepository userRepository;

    public LoginViewModel() {
        userRepository = new UserRepository();
    }

    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }

    public LiveData<Boolean> isLoginSuccessful() {
        return isLoginSuccessful;
    }

    public void loginUser(String email, String password) {
        if (email.isEmpty() || password.isEmpty()) {
            errorMessage.setValue("Please complete all fields.");
            return;
        }

        userRepository.loginUser(email, password, new UserRepository.OnLoginListener() {
            @Override
            public void onSuccess() {
                isLoginSuccessful.setValue(true);
            }

            @Override
            public void onFailure(Exception e) {
                errorMessage.setValue("Error in authentication: " + e.getMessage());
            }
        });
    }

    public void resetLoginState() {
        isLoginSuccessful.setValue(null);
    }
}

