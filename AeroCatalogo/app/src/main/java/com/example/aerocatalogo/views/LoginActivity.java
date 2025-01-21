package com.example.aerocatalogo.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.viewmodels.LoginViewModel;

public class LoginActivity extends AppCompatActivity {
    private LoginViewModel loginViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        loginViewModel = new ViewModelProvider(this).get(LoginViewModel.class);

        // Observadores
        loginViewModel.getErrorMessage().observe(this, errorMessage -> {
            if (errorMessage != null) {
                Toast.makeText(LoginActivity.this, errorMessage, Toast.LENGTH_SHORT).show();
            }
        });

        loginViewModel.isLoginSuccessful().observe(this, isSuccessful -> {
            if (isSuccessful != null && isSuccessful) {
                Toast.makeText(LoginActivity.this, "Login successful.", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(LoginActivity.this, DashboardActivity.class);
                startActivity(intent);
            }
        });


        // Configurar botones
        findViewById(R.id.loginButton).setOnClickListener(v -> {
            String email = ((EditText) findViewById(R.id.emailEditText)).getText().toString();
            String password = ((EditText) findViewById(R.id.passwordEditText)).getText().toString();

            // Delegar el inicio de sesión al ViewModel
            loginViewModel.loginUser(email, password);
        });

        findViewById(R.id.createAccountButton).setOnClickListener(v -> {
            Intent intent = new Intent(LoginActivity.this, RegisterActivity.class);
            startActivity(intent);
        });
    }
}