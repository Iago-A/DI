package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.viewmodels.RegisterViewModel;


public class RegisterActivity extends AppCompatActivity {
    private RegisterViewModel registerViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        registerViewModel = new ViewModelProvider(this).get(RegisterViewModel.class);

        // Observadores para los resultados
        registerViewModel.getErrorMessage().observe(this, errorMessage -> {
            if (errorMessage != null) {
                Toast.makeText(RegisterActivity.this, errorMessage, Toast.LENGTH_SHORT).show();
            }
        });

        registerViewModel.isRegistrationSuccessful().observe(this, isSuccessful -> {
            if (isSuccessful != null && isSuccessful) {
                Toast.makeText(RegisterActivity.this, "User registered successfully", Toast.LENGTH_SHORT).show();
                finish();
            }
        });

        // Configurar el botón de registro
        findViewById(R.id.registerButton).setOnClickListener(v -> {
            String fullName = ((EditText) findViewById(R.id.fullNameEditText)).getText().toString();
            String email = ((EditText) findViewById(R.id.emailEditText)).getText().toString();
            String phone = ((EditText) findViewById(R.id.phoneEditText)).getText().toString();
            String address = ((EditText) findViewById(R.id.addressEditText)).getText().toString();
            String password = ((EditText) findViewById(R.id.passwordEditText)).getText().toString();
            String confirmPassword = ((EditText) findViewById(R.id.confirmPasswordEditText)).getText().toString();

            // Delegar la validación y registro al ViewModel
            registerViewModel.registerUser(fullName, email, phone, address, password, confirmPassword);
        });
    }
}
