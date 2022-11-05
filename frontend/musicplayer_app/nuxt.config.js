import colors from 'vuetify/es5/util/colors'
const HOST = 'localhost'
const DEFAULT_BASE_URL = `http://${HOST}:8000`

export default {
  components: true,  	
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Fox Music',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  loading: {
    color: '#2196F3',
    height: '3px'
  },
  server: {
    host: HOST,
    port: 3000
  },

  env: {
    baseUrl: process.env.BASE_URL || DEFAULT_BASE_URL,
    csrftoken: 'csrftoken',
    songsAPI: '/api/songs/',
    playsAPI: '/api/plays/',
    genresAPI: '/api/genres/',
    artistsAPI: '/api/artists/',
    authAPI: '/api/token-auth/',
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~assets/styles.scss',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
	  '~/plugins/axios-accessor.ts'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
	  '@nuxtjs/composition-api/module'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
	'@nuxtjs/axios',
  'cookie-universal-nuxt',
  ],

  axios: {
    baseURL: DEFAULT_BASE_URL, // Used as fallback if no runtime config is provided
  },

  publicRuntimeConfig: {
	axios: {
	  browserBaseURL: process.env.BROWSER_BASE_URL
	}
  },

  privateRuntimeConfig: {
    axios: {
	  baseURL: process.env.BASE_URL
    }
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  watchers: {
    webpack: {
      aggregateTimeout:300,
      poll: 1000
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    postcss: null,
  }
}
