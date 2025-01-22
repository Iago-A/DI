package com.example.aerocatalogo.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.adapters.PlaneAdapter;
import com.example.aerocatalogo.models.Plane;
import com.example.aerocatalogo.viewmodels.DashboardViewModel;
import com.google.firebase.auth.FirebaseAuth;

import java.util.ArrayList;


public class DashboardActivity extends AppCompatActivity {

    private DashboardViewModel viewModel;
    private PlaneAdapter adapter;
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        // Inicializar FirebaseAuth
        mAuth = FirebaseAuth.getInstance();

        // Configurar RecyclerView
        RecyclerView recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        // Inicializar adapter con lista vacía
        adapter = new PlaneAdapter(new ArrayList<>(), this::openDetailActivity);
        recyclerView.setAdapter(adapter);

        // Configurar ViewModel
        viewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        // Observar cambios en la lista de aviones
        viewModel.getPlanes().observe(this, planes -> {
            adapter = new PlaneAdapter(planes, this::openDetailActivity);
            recyclerView.setAdapter(adapter);
        });

        // Observar errores
        viewModel.getError().observe(this, error -> {
            if (error != null) {
                Toast.makeText(this, error, Toast.LENGTH_LONG).show();
            }
        });

        Button logoutButton = findViewById(R.id.logoutButton);
        logoutButton.setOnClickListener(v -> {
            // Limpiar ViewModel
            getViewModelStore().clear();
            mAuth.signOut();
            Toast.makeText(this, "Logout correctly", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(this, LoginActivity.class));
            finish();
        });
    }

    private void openDetailActivity(Plane plane) {
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("plane_title", plane.getTitle());
        intent.putExtra("plane_description", plane.getDescription());
        intent.putExtra("plane_url", plane.getUrl());
        startActivity(intent);
    }
}




//        // Inicializar vistas
//        TextView titleTextView = findViewById(R.id.titleTextView);
//        TextView descriptionTextView = findViewById(R.id.descriptionTextView);
//        ImageView imageView = findViewById(R.id.imageView);
//        Button logoutButton = findViewById(R.id.logoutButton);
//
//        // Configurar botón de logout
//        logoutButton.setOnClickListener(v -> {
//            mAuth.signOut();
//            Toast.makeText(this, "You closed your session", Toast.LENGTH_SHORT).show();
//            finish();
//        });
//
//        // Obtener datos de Firebase
//        DatabaseReference databaseRef = FirebaseDatabase.getInstance().getReference("pictures").child("picture1");
//
//        databaseRef.addListenerForSingleValueEvent(new ValueEventListener() {
//            @Override
//            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
//                if (dataSnapshot.exists()) {
//                    // Obtener valores
//                    String title = dataSnapshot.child("title").getValue(String.class);
//                    String description = dataSnapshot.child("description").getValue(String.class);
//                    String imageUrl = dataSnapshot.child("url").getValue(String.class);
//
//                    // Actualizar UI
//                    titleTextView.setText(title);
//                    descriptionTextView.setText(description);
//
//                    // Cargar imagen usando Glide
//                    if (imageUrl != null && !imageUrl.isEmpty()) {
//                        Glide.with(DashboardActivity.this)
//                                .load(imageUrl)
//                                .into(imageView);
//                    }
//                }
//            }
//
//            @Override
//            public void onCancelled(@NonNull DatabaseError error) {
//                Toast.makeText(DashboardActivity.this,
//                        "Error al cargar datos: " + error.getMessage(),
//                        Toast.LENGTH_SHORT).show();
//            }
//        });
//    }
//}
