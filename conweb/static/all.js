// Generated by CoffeeScript 1.4.0
(function() {
  var App;

  App = angular.module('App', ['ngAnimate']);

  App.config(function($httpProvider) {
    return $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  });

  App.controller('base', function($rootScope, $scope) {
    $rootScope.slidePageUrl = '';
    $rootScope.closePage = function(event) {
      if ($rootScope.slidePageUrl === '') {
        return;
      }
      $rootScope.slidePageUrl = '';
    };
    return $scope.btnNavText = function() {
      if ($scope.showNav) {
        return '✕';
      } else {
        return 'N';
      }
    };
  });

  App.directive('turbolink', function($http, $rootScope, $document) {
    return {
      restrict: 'A',
      scope: false,
      link: function(scope, element, attrs) {
        element.on('click', function(event) {
          event.preventDefault();
          if ($rootScope.slidePageUrl !== '') {
            return;
          }
          event.stopPropagation();
          $rootScope.slidePageUrl = attrs.href;
          return scope.$digest();
        });
      }
    };
  });

}).call(this);
