{% load static %}

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Programist.FREE</title>

  <link href="{% static 'css/base.css' %}" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700&display=swap" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/vuetify@3.4.0/dist/vuetify.min.css" rel="stylesheet" />
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@3.4.0/dist/vuetify.min.js"></script>
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />

  <style>
    body {
      font-family: 'Source Sans Pro', sans-serif;
    }
    .v-toolbar-title {
      font-weight: bold;
      font-size: 1.5rem;
    }
    .v-container {
      max-width: 900px;
    }
  </style>
</head>

<body>
  <div id="app">
    <v-app>
      <v-theme-provider theme="dark">
        
        <!-- Navigation Drawer -->
        <v-navigation-drawer v-model="drawer" temporary>
          <v-list>
            <v-list-item prepend-icon="mdi-home" title="Дом" href="{% url 'home' %}"></v-list-item>
            <v-list-item prepend-icon="mdi-function" title="Функции" href="#features"></v-list-item>
            <v-list-item prepend-icon="mdi-cash" title="Цены" href="#pricing"></v-list-item>
            <v-list-item prepend-icon="mdi-information" title="О" href="#about"></v-list-item>
          </v-list>
        </v-navigation-drawer>

        <!-- App Bar -->
        <v-app-bar color="grey-darken-4" elevation="4">
          <template v-slot:prepend>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
          </template>

          <v-app-bar-title class="text-yellow-lighten-1">
            <v-icon start>mdi-rocket-launch</v-icon>Programist.FREE
          </v-app-bar-title>

          <template v-slot:append>
            <v-text-field
              v-model="searchQuery"
              density="compact"
              variant="solo"
              label="Поиск"
              append-inner-icon="mdi-magnify"
              single-line
              hide-details
              @click:append-inner="search"
              style="max-width: 200px;"
            ></v-text-field>
          </template>
        </v-app-bar>

        <!-- Main Content -->
        <v-main>
          <v-container class="text-white py-10">
            {% if user.is_authenticated %}
              <div class="mb-4">
                <v-btn href="{% url 'post_new' %}" color="amber" variant="flat">
                  Сделай вакансию!
                </v-btn>
              </div>
              <p>Привет, {{ user.username }}!</p>
            {% else %}
              <p>Вы не вошли в систему.</p>
              <v-btn href="{% url 'login' %}" color="white" variant="text">Войти</v-btn>
            {% endif %}

            {% block content %}
            {% endblock %}
          </v-container>
        </v-main>

      </v-theme-provider>
    </v-app>
  </div>

  <!-- Vue/Vuetify Init -->
  <script>
    const { createApp, ref } = Vue;
    const vuetify = Vuetify.createVuetify({
      icons: { defaultSet: 'mdi' },
      theme: { defaultTheme: 'dark' },
    });

    createApp({
      setup() {
        const drawer = ref(false);
        const searchQuery = ref('');
        const search = () => {
          console.log('Поиск:', searchQuery.value);
        };
        return { drawer, searchQuery, search };
      }
    }).use(vuetify).mount('#app');
  </script>
</body>
</html>
