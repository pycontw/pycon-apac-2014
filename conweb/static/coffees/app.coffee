App = angular.module('App', ['ngAnimate'])

App.config ($httpProvider)->
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

App.controller 'base', ($rootScope, $scope)->
  $rootScope.slidePageUrl = ''

  $rootScope.closePage = (event)->
    if $rootScope.slidePageUrl == ''
      return
    $rootScope.slidePageUrl = ''
    return

  $scope.btnNavText = ()->
    if $scope.showNav
      return '✕'
    else
      return 'N'

  $scope.$on '$includeContentRequested', ()->
    $scope.loading = true

  $scope.$on '$includeContentLoaded', ()->
    $scope.loading = false


App.directive 'turbolink', ($http, $rootScope, $document)->
  return {
    restrict: 'A'
    scope: false
    link: (scope, element, attrs)->
      element.on 'click', (event)->
        event.preventDefault()
        if $rootScope.slidePageUrl != ''
          return
        event.stopPropagation()
        $rootScope.slidePageUrl = attrs.href
        scope.$digest()

      return
  }
