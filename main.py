<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Annuaire des Boutiques</title>
    <style>
        /* Un style propre et moderne */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        /* Barre de navigation / Filtres */
        .filters {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 30px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            background-color: #ddd;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s;
        }
        button:hover, button.active {
            background-color: #007bff;
            color: white;
        }
        /* Grille des boutiques */
        #shop-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            max-width: 1000px;
            margin: 0 auto;
        }
        /* Carte de boutique */
        .shop-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }
        .category-badge {
            display: inline-block;
            margin-top: 10px;
            padding: 5px 10px;
            background-color: #eee;
            border-radius: 12px;
            font-size: 0.8em;
            color: #555;
        }
    </style>
</head>
<body>

    <h1>Nos Boutiques</h1>

    <div class="filters">
        <button class="active" onclick="filterShops('TOUT')">TOUT</button>
        <button onclick="filterShops('LUXE')">LUXE</button>
        <button onclick="filterShops('TECH')">TECH</button>
        <button onclick="filterShops('MODE')">MODE</button>
        <button onclick="filterShops('SPORT')">SPORT</button>
        <button onclick="filterShops('BEAUTE')">BEAUTÉ</button>
        <button onclick="filterShops('MAISON')">MAISON</button>
        <button onclick="filterShops('AUTO')">AUTO</button>
        <button onclick="filterShops('DIVERS')">DIVERS</button>
    </div>

    <div id="shop-container"></div>

    <script>
        // Fausse base de données pour tester (en attendant ton Excel/Turso)
        const shops = [
            { name: "ZARA", category: "MODE" },
            { name: "Apple Store", category: "TECH" },
            { name: "Sephora", category: "BEAUTE" },
            { name: "Rolex", category: "LUXE" },
            { name: "Decathlon", category: "SPORT" },
            { name: "Ikea", category: "MAISON" },
            { name: "Boulanger", category: "TECH" },
            { name: "Norauto", category: "AUTO" },
            { name: "Fnac", category: "DIVERS" },
            { name: "Louis Vuitton", category: "LUXE" },
            { name: "Nike", category: "SPORT" }
        ];

        // Fonction pour afficher les boutiques
        function renderShops(shopList) {
            const container = document.getElementById('shop-container');
            container.innerHTML = ''; // On vide le conteneur

            // Tri de A à Z
            shopList.sort((a, b) => a.name.localeCompare(b.name));

            // On crée les cartes pour chaque boutique
            shopList.forEach(shop => {
                const card = document.createElement('div');
                card.className = 'shop-card';
                card.innerHTML = `
                    <h3>${shop.name}</h3>
                    <span class="category-badge">${shop.category}</span>
                `;
                container.appendChild(card);
            });
        }

        // Fonction pour filtrer selon l'onglet cliqué
        function filterShops(category) {
            // Mettre à jour le bouton actif (visuel)
            document.querySelectorAll('.filters button').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');

            // Filtrer les données
            if (category === 'TOUT') {
                renderShops(shops);
            } else {
                const filtered = shops.filter(shop => shop.category === category);
                renderShops(filtered);
            }
        }

        // Afficher "TOUT" au chargement de la page
        renderShops(shops);
    </script>
</body>
</html>
