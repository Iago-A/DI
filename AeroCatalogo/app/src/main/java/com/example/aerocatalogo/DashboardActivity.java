package com.example.aerocatalogo;

import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class DashboardActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        mAuth = FirebaseAuth.getInstance();

        // Inicializar vistas
        TextView titleTextView = findViewById(R.id.titleTextView);
        TextView descriptionTextView = findViewById(R.id.descriptionTextView);
        ImageView imageView = findViewById(R.id.imageView);
        Button logoutButton = findViewById(R.id.logoutButton);

        // Configurar botón de logout
        logoutButton.setOnClickListener(v -> {
            mAuth.signOut();
            Toast.makeText(this, "You closed your session", Toast.LENGTH_SHORT).show();
            finish();
        });

        // Obtener datos de Firebase
        DatabaseReference databaseRef = FirebaseDatabase.getInstance().getReference("pictures").child("picture1");

        databaseRef.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                if (dataSnapshot.exists()) {
                    // Obtener valores
                    String title = dataSnapshot.child("title").getValue(String.class);
                    String description = dataSnapshot.child("description").getValue(String.class);
                    String imageUrl = dataSnapshot.child("url").getValue(String.class);

                    // Actualizar UI
                    titleTextView.setText(title);
                    descriptionTextView.setText(description);

                    // Cargar imagen usando Glide
                    if (imageUrl != null && !imageUrl.isEmpty()) {
                        Glide.with(DashboardActivity.this)
                                .load(imageUrl)
                                .into(imageView);
                    }
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(DashboardActivity.this,
                        "Error al cargar datos: " + error.getMessage(),
                        Toast.LENGTH_SHORT).show();
            }
        });
    }
}
