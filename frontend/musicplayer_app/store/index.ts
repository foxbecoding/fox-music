import { GetterTree, ActionTree, MutationTree } from 'vuex'

export const state = () => ({
    auth_token: '',
    show_snackbar: false,
    snackbar_text: ''
})

export type RootState = ReturnType<typeof state>

export const getters: GetterTree<RootState, RootState> = {
    auth_token: state => state.auth_token as string,
    snackbar_text: state => state.snackbar_text as string,
    show_snackbar: state => state.show_snackbar as boolean
}

export const mutations: MutationTree<RootState> = {
    auth_token(state: RootState, token: string): void{
        state.auth_token = token
    },
    snackbar(state: RootState, data): void{
        state.snackbar_text = data.text
        state.show_snackbar = data.show
    },
}

export const actions: ActionTree<RootState, RootState> = {
 
}