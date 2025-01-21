package com.example.aerocatalogo.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.aerocatalogo.repositories.UserRepository;

public class RegisterViewModel extends ViewModel {
    private final MutableLiveData<String> errorMessage = new MutableLiveData<>();
    private final MutableLiveData<Boolean> isRegistrationSuccessful = new MutableLiveData<>();
    private final UserRepository userRepository;

    public RegisterViewModel() {
        userRepository = new UserRepository();
    }

    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }

    public LiveData<Boolean> isRegistrationSuccessful() {
        return isRegistrationSuccessful;
    }

    public void registerUser(String fullName, String email, String phone, String address, String password, String confirmPassword) {
        // Validaciones
        if (fullName.isEmpty() || email.isEmpty() || phone.isEmpty() || address.isEmpty() || password.isEmpty() || confirmPassword.isEmpty()) {
            errorMessage.setValue("All fields must be filled");
            return;
        }

        if (!password.equals(confirmPassword)) {
            errorMessage.setValue("Passwords do not match");
            return;
        }

        if (password.length() < 6) {
            errorMessage.setValue("Password must be at least 6 characters long");
            return;
        }

        // Si las validaciones pasan, registrar al usuario en UserRepository
        userRepository.registerUser(fullName, email, phone, address, password, new UserRepository.OnUserRegisteredListener() {
            @Override
            public void onSuccess() {
                isRegistrationSuccessful.setValue(true);
            }

            @Override
            public void onFailure(Exception e) {
                errorMessage.setValue("Error registering user: " + e.getMessage());
            }
        });
    }
}

